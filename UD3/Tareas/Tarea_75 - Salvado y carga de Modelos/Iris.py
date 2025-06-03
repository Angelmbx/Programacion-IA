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
    def __init__(self, src_file, transform=None):
        irisDataset = pd.read_csv(
            src_file,
            header=0,
            names=["sepallength", "sepalwidth", "petallength", "petalwidth", "class"],
        )
        X = irisDataset[["sepallength", "sepalwidth", "petallength", "petalwidth"]]
        Y = irisDataset[["class"]]

        X = X.apply(pd.to_numeric, errors="coerce")
        
        unique_classes = Y["class"].unique()
        YConversion = pd.DataFrame(
            {cls: (Y["class"] == cls).astype(float) for cls in unique_classes}
        )
        y_tensor = torch.tensor(YConversion.to_numpy(), dtype=torch.float32)

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
        features = self.data[idx, :4]
        labels = self.data[idx, 4:]
        sample = (features, labels)
        if self.transform:
            sample = self.transform(sample)
        return sample

dataset = IrisDataset("Iris.csv")
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
        self.layer1 = nn.Linear(input_dim, 16)
        self.layer2 = nn.Linear(16, 8)
        self.layer3 = nn.Linear(8, 3)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.softmax(self.layer3(x), dim=1)
        return x

model = Model(4)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

print(model)

entradaProba, dest = next(iter(train_loader))
print(entradaProba)
print(dest)
saida = model(entradaProba)
print(saida)
loss_val = loss_fn(saida, torch.argmax(dest, dim=1))
print("Loss:", loss_val.item())

def train_one_epoch(epoch_index):
    running_loss = 0.0
    last_loss = 0.0
    for i, data in enumerate(train_loader):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, torch.argmax(labels, dim=1))
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        if i % 10 == 9:
            last_loss = running_loss / 10
            print(f"  Batch {i+1} loss: {last_loss:.4f}")
            running_loss = 0.0
    return last_loss

EPOCHS = 100
loss_list = []
accuracy_list = []

for epoch in range(EPOCHS):
    print(f"EPOCH {epoch+1}:")
    model.train()
    avg_loss = train_one_epoch(epoch)
    loss_list.append(avg_loss)
    
    model.eval()
    running_vloss = 0.0
    correct_total = 0
    total_val = 0
    with torch.no_grad():
        for vinputs, vlabels in validation_loader:
            voutputs = model(vinputs)
            vloss = loss_fn(voutputs, torch.argmax(vlabels, dim=1))
            running_vloss += vloss.item()
            preds = torch.argmax(voutputs, dim=1)
            labels = torch.argmax(vlabels, dim=1)
            correct_total += (preds == labels).sum().item()
            total_val += labels.size(0)
    avg_vloss = running_vloss / len(validation_loader)
    accuracy = correct_total / total_val
    accuracy_list.append(accuracy)
    print(f"Train loss: {avg_loss:.4f}, Validation loss: {avg_vloss:.4f}, Accuracy: {accuracy:.4f}")
    
torch.save(model, "modelo_entrenado.pt")