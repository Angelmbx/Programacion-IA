import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, random_split
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

class StandardScaler:
    def __init__(self, mean=None, std=None, epsilon=1e-7):
        self.mean = mean
        self.std = std
        self.epsilon = epsilon

    def fit(self, values):
        dims = list(range(values.dim() - 1))
        self.mean = torch.mean(values, dim=dims)
        self.std = torch.std(values, dim=dims)

    def transform(self, values):
        return (values - self.mean) / (self.std + self.epsilon)

    def fit_transform(self, values):
        self.fit(values)
        return self.transform(values)

    def __repr__(self):
        return f"mean: {self.mean}, std: {self.std}, epsilon: {self.epsilon}"
    
class AutomovilDataset(Dataset):
    def __init__(self, src_file, transform=None):
        df = pd.read_csv(src_file, 
                        header=None, sep=",",
                        names = [
                                "symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", 
                                "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", 
                                "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", 
                                "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"
                            ])


        # Cambia '?' por NaN 
        df.replace("?", pd.NA, inplace=True)
        df = df.apply(pd.to_numeric, errors='ignore')  # deja las categóricas como strings
        
        # Elimina filas donde falta el target
        df = df[df['price'].notna()]
        df['price'] = pd.to_numeric(df['price'])  

        # Sustituye nulos por la media en los datos numéricos
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.mean()))
        
        # En los categóricos por la moda
        categorical_cols = df.select_dtypes(include='object').columns
        df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))
    
        # One-Hot Encoding
        df = pd.get_dummies(df, columns=categorical_cols)

        X = df.loc[:, ~df.columns.isin(['price'])]
        Y = df[["price"]]
        
        # Convertir a tensores
        x_tensor = torch.tensor(X.values.astype("float32"), dtype=torch.float32)
        y_tensor = torch.tensor(Y.values.astype("float32"), dtype=torch.float32)

        # Escalado
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(x_tensor).type(torch.float32)

        self.data = torch.cat((X_scaled, y_tensor), 1)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        features = self.data[idx, :-1]
        labels = self.data[idx, -1:]
        sample = (features, labels)
        if self.transform:
            sample = self.transform(sample)
        return sample

dataset = AutomovilDataset("imports-85.data")


lonxitudeDataset = len(dataset)
tamTrain =int(lonxitudeDataset*0.8)
tamVal = lonxitudeDataset - tamTrain
print(f"Tamaño dataset: {lonxitudeDataset} conjunto de entrenamiento: {tamTrain} conjunto de validación: {tamVal}")
train_set, val_set = random_split(dataset,[tamTrain,tamVal])
train_loader = torch.utils.data.DataLoader(train_set, batch_size=2,shuffle=True, drop_last=False)
validation_loader =torch.utils.data.DataLoader(val_set, batch_size=4, shuffle=False) 