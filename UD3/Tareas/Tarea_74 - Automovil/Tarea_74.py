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
        bostonDataset = pd.read_csv(src_file, delim_whitespace=True,names=['Frequency','Angle of attack','Chord length', 'Free-stream velocity', 'Suction side displacement thickness', 'Pressure level'])
        X = bostonDataset.loc[:, ~bostonDataset.columns.isin(['Pressure level'])]
        Y = bostonDataset[["Pressure level"]]
    
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

dataset = AutomovilDataset("imports-85.data")