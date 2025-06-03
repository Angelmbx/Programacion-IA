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

class IrisDataset(Dataset):
    def __init__(self, src_file):
        dataset = pd.read_csv(src_file, header=0)  
        X = dataset[["sepallength", "sepalwidth", "petallength", "petalwidth"]]
        
        s1 = X.values.astype("float32")
        x_tensor = torch.tensor(s1, dtype=torch.float32)
        
        # vuelvo a escalar?
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(x_tensor).type(torch.float32)
        self.data = X_scaled
        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        features = self.data[idx]
        sample = features  # Ahora no hay etiqueta 'y', solo features
        if self.transform:
            sample = self.transform(sample)
        return sample

dataset = IrisDataset("Iris_modificado.csv")
print(f"Dataset size: {len(dataset)}")


# Carga del modelo
model = torch.load("modelo_entrenado.pt")
model.eval() 
salida = model(tensor_entrada) # ?