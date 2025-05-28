import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
import matplotlib.pyplot as plt

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
    
class BostonDataset(Dataset):
    def __init__(self, src_file, transform=None):
        bostonDataset = pd.read_csv(src_file, delim_whitespace=True,names=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'])
        X = bostonDataset.loc[:, ~bostonDataset.columns.isin(['MEDV'])]
        Y = bostonDataset[["MEDV"]]
    
        X = X.apply(pd.to_numeric, errors="coerce")
        
        y_tensor = torch.tensor(Y.values.astype("float32"), dtype=torch.float32)
        
        s1 = X.values.astype("float32")
        x_tensor = torch.tensor(s1, dtype=torch.float32)

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

dataset = BostonDataset("housing.data")

# División Train - Test del dataset 
from torch.utils.data import random_split

lonxitudeDataset = len(dataset)
tamTrain =int(lonxitudeDataset*0.8)
tamVal = lonxitudeDataset - tamTrain
print(f"Tamaño dataset: {lonxitudeDataset} conjunto de entrenamiento: {tamTrain} conjunto de validación: {tamVal}")
train_set, val_set = random_split(dataset,[tamTrain,tamVal])
train_loader = torch.utils.data.DataLoader(train_set, batch_size=2,shuffle=True, drop_last=False)
validation_loader =torch.utils.data.DataLoader(val_set, batch_size=4, shuffle=False)    


