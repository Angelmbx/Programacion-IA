import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import numpy as np

# Cargar los datos
data = pd.read_csv('sonar.csv', header=None)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Codificar etiquetas ('M' = 1, 'R' = 0)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Normalizar las características
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convertir a tensores
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test  = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
y_test  = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Definir la red neuronal
class SonarNN(nn.Module):
    def __init__(self):
        super(SonarNN, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(60, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

# Instanciar modelo, función de pérdida y optimizador
model = SonarNN()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Entrenar
epochs = 100
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f"Época {epoch+1}/{epochs}, Pérdida: {loss.item():.4f}")

# Evaluar
model.eval()
with torch.no_grad():
    predictions = model(X_test)
    predicted = (predictions >= 0.5).float()
    accuracy = (predicted == y_test).float().mean()
    print(f"\nPrecisión en test: {accuracy.item()*100:.2f}%")
