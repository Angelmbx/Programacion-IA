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
        df = pd.read_csv(src_file, header=None, sep=",")
 
        # Reemplazar '?' por NaN y convertir todas a tipo apropiado
        df.replace("?", pd.NA, inplace=True)
        df = df.apply(pd.to_numeric, errors='ignore')  # deja las categóricas como strings
        
        # Eliminar filas donde falta el target
        df = df[df['price'].notna()]
        df['price'] = pd.to_numeric(df['price'])  # asegurar tipo numérico en target

        # Rellenar valores numéricos faltantes con media
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].apply(lambda x: x.fillna(x.mean()))
        
        # Rellenar categóricos faltantes con moda
        categorical_cols = df.select_dtypes(include='object').columns
        df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))
        
        # Convertir categóricas a variables dummy (One-Hot Encoding)
        df = pd.get_dummies(df, columns=categorical_cols)
        
        X = df.iloc[:, :-1]  
        Y = df.iloc[:, -1:]  # Target = ultima columna
        
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