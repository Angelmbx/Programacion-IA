import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter
import torchmetrics

writer = SummaryWriter("./log")
train_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=2)
val_accuracy = torchmetrics.Accuracy(task="multiclass", num_classes=2)

class StandardScaler:
    def __init__(self, epsilon=1e-7):
        self.mean = None
        self.std = None
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

class SonarDataset(Dataset):
    def __init__(self, src_file, transform=None):
        sonarDataset = pd.read_csv(src_file, header=0)
        X = sonarDataset.iloc[:, :-1]
        Y = sonarDataset.iloc[:, -1]
        
        unique_classes = sorted(Y.unique())
        print("Clases detectadas:", unique_classes)
        if set(unique_classes) != {"M", "R"}:
            raise ValueError("El dataset tiene clases inesperadas.")

        X = X.apply(pd.to_numeric, errors="coerce")
        
        YConversion = pd.DataFrame({cls: (Y == cls).astype(float) for cls in ["M", "R"]})
        print("One-hot encoding de etiquetas:")
        print(YConversion.head())
        
        y_tensor = torch.tensor(YConversion.to_numpy(), dtype=torch.float32)
        x_tensor = torch.tensor(X.values.astype("float32"), dtype=torch.float32)

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(x_tensor).type(torch.float32)
        
        self.data = torch.cat((X_scaled, y_tensor), 1)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        features = self.data[idx, :-2]
        labels = self.data[idx, -2:]
        sample = (features, labels)
        if self.transform:
            sample = self.transform(sample)
        return sample

dataset = SonarDataset("tarefa 70/sonar/sonar.all-data")
print(dataset[0])
print(f"Dataset size: {len(dataset)}")

total_size = len(dataset)
train_size = int(total_size * 0.8)
val_size = total_size - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
print(f"Train size: {train_size}, Validation size: {val_size}")

batch_size = 16
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
validation_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

class Model(nn.Module):
    def __init__(self, input_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Linear(input_dim, 50)
        self.layer2 = nn.Linear(50, 50)
        self.layer3 = nn.Linear(50, 2)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = self.layer3(x)  # Remove softmax here
        return x

model = Model(60)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

entradaProba, dest = next(iter(train_loader))
writer.add_graph(model, entradaProba)

saida = model(entradaProba)
print("Salida de la red:", saida.shape)
loss_val = loss_fn(saida, torch.argmax(dest, dim=1))
print("Loss inicial:", loss_val.item())

def train_one_epoch(epoch_index):
    running_loss = 0.0
    for i, data in enumerate(train_loader):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, torch.argmax(labels, dim=1))
        loss.backward()
        optimizer.step()
        train_accuracy.update(torch.argmax(outputs, dim=1), torch.argmax(labels, dim=1))
        running_loss += loss.item()
        if i % 10 == 9:
            avg_loss = running_loss / 10
            writer.add_scalar('Training loss/batch', avg_loss, epoch_index * len(train_loader) + i)
            print(f"  Batch {i+1} loss: {avg_loss:.4f}")
            running_loss = 0.0

EPOCHS = 100
best_accuracy = 0.0
for epoch in range(EPOCHS):
    print(f"EPOCH {epoch+1}:")
    model.train()
    train_accuracy.reset()
    train_one_epoch(epoch)
    model.eval()
    val_loss = 0.0
    val_accuracy.reset()
    
    with torch.no_grad():
        for vinputs, vlabels in validation_loader:
            voutputs = model(vinputs)
            loss = loss_fn(voutputs, torch.argmax(vlabels, dim=1))
            val_loss += loss.item()
            val_accuracy.update(torch.argmax(voutputs, dim=1), torch.argmax(vlabels, dim=1))
    
    avg_val_loss = val_loss / len(validation_loader)
    epoch_val_accuracy = val_accuracy.compute().item()
    
    writer.add_scalar('Validation/Accuracy', epoch_val_accuracy, epoch)
    writer.add_scalar('Validation/Loss', avg_val_loss, epoch)
    
    if epoch % 10 == 0:
        for name, param in model.named_parameters():
            writer.add_histogram(name, param, epoch)
    
    print(f"Validation Accuracy: {epoch_val_accuracy:.4f}")

    if epoch_val_accuracy > best_accuracy:
        best_accuracy = epoch_val_accuracy
        torch.save(model.state_dict(), 'best_model.pth')
        
writer.close()
