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
    
    
class AirfoilDataset(Dataset):
    def __init__(self, src_file, transform=None):
        airfolDataset = pd.read_csv(src_file, delim_whitespace=True,names=['Frequency','Angle of attack','Chord length', 'Free-stream velocity', 'Suction side displacement thickness', 'Pressure level'])
        X = airfolDataset.loc[:, ~airfolDataset.columns.isin(['Pressure level'])]
        Y = airfolDataset[["Pressure level"]]
    
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

dataset = AirfoilDataset("airfoil_self_noise.dat")

# División Train - Test del dataset 

lonxitudeDataset = len(dataset)
tamTrain =int(lonxitudeDataset*0.8)
tamVal = lonxitudeDataset - tamTrain
print(f"Tamaño dataset: {lonxitudeDataset} conjunto de entrenamiento: {tamTrain} conjunto de validación: {tamVal}")
train_set, val_set = random_split(dataset,[tamTrain,tamVal])
train_loader = torch.utils.data.DataLoader(train_set, batch_size=2,shuffle=True, drop_last=False)
validation_loader =torch.utils.data.DataLoader(val_set, batch_size=4, shuffle=False) 

class Model(nn.Module):
    def __init__(self, entradas):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(entradas, 100)
        self.layer2 = nn.Linear(100, 50)
        self.layer3 = nn.Linear(in_features=50, out_features=1)
        
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.relu(self.layer3(x))
        return x
    
model     = Model(5)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn   = nn.MSELoss(reduction='sum')
print(model)

# Simulacion de una iteración

entradaProba,dest = next(iter(train_loader))
print("Entrada:")
print(entradaProba)
print("Desexada:")
print(dest)
saida = model(entradaProba) 
print("Saída:")
print(saida)
loss_fn(saida, dest)

def train_one_epoch(epoch_index, tb_writer):
    running_loss = 0.
    for i, data in enumerate(train_loader):
        # Every data instance is an input + label pair
        inputs, labels = data

        # Zero your gradients for every batch!
        optimizer.zero_grad()

        # Make predictions for this batch
        outputs = model(inputs)

        # Compute the loss and its gradients
        loss = loss_fn(outputs, labels)
        loss.backward()

        # Adjust learning weights
        optimizer.step()

        # Gather data and report
        running_loss += loss.item()

    return running_loss / len(train_loader)

# Funcion para evaluar entrenamiento
def evaluate(val_loader):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, labels in val_loader:
            outputs = model(inputs)
            loss = loss_fn(outputs, labels)
            total_loss += loss.item()
    return total_loss / len(val_loader)


EPOCHS = 200
writer = SummaryWriter(log_dir="./runs/Airfoil_Self-Noise")

# Entrenamiento
for epoch in range(EPOCHS):
    model.train(True)
    avg_loss = train_one_epoch(epoch, writer)
    val_loss = evaluate(validation_loader)

    print(f"Epoch {epoch+1}/{EPOCHS} - Train loss: {avg_loss:.4f} - Val loss: {val_loss:.4f}")

    writer.add_scalar('Loss/train', avg_loss, epoch)
    writer.add_scalar('Loss/validation', val_loss, epoch)
    
writer.close()