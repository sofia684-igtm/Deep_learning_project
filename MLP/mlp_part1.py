# ==============================
# 1. IMPORTS
# ==============================
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

import torch
import torch.nn as nn
import torch.optim as optim

# ==============================
# 2. DEVICE CPU / GPU
# ==============================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device utilisé :", device)

# ==============================
# 3. CHARGER DATASET
# ==============================
data = load_breast_cancer()

X = data.data
y = data.target

# ==============================
# 4. SPLIT TRAIN / TEST
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==============================
# 5. NORMALISATION
# ==============================
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================
# 6. CONVERSION PYTORCH
# ==============================
X_train = torch.tensor(
    X_train,
    dtype=torch.float32
).to(device)

X_test = torch.tensor(
    X_test,
    dtype=torch.float32
).to(device)

y_train = torch.tensor(
    y_train,
    dtype=torch.long
).to(device)

y_test = torch.tensor(
    y_test,
    dtype=torch.long
).to(device)

# ==============================
# 7. VÉRIFICATION
# ==============================
print("Train shape :", X_train.shape)
print("Test shape  :", X_test.shape)

# ==============================
# 8. MODÈLE CUSTOM MLP
# ==============================
class MonMLP(nn.Module):

    def __init__(self):
        super(MonMLP, self).__init__()

        self.fc1 = nn.Linear(30, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 2)

        self.relu = nn.ReLU()

    def forward(self, x):

        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)

        return x


model = MonMLP().to(device)

# ==============================
# VERSION MLP AVEC nn.Sequential
# ==============================

model_sequential = nn.Sequential(
    nn.Linear(30, 16),
    nn.ReLU(),
    nn.Linear(16, 8),
    nn.ReLU(),
    nn.Linear(8, 2)
).to(device)

print("\n===== MLP SEQUENTIAL =====")
print(model_sequential)

# ==============================
# 9. INITIALISATIONS
# ==============================

# Xavier Initialization
def init_xavier(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_uniform_(m.weight)

# Gaussian Initialization
def init_gaussian(m):
    if isinstance(m, nn.Linear):
        nn.init.normal_(m.weight, mean=0, std=0.01)

# Constant Initialization
def init_constant(m):
    if isinstance(m, nn.Linear):
        nn.init.constant_(m.weight, 0.5)

# ==============================
# CHOISIR UNE INITIALISATION
# ==============================

# TEST 1 : Xavier
model.apply(init_gaussian)

# Pour tester Gaussian :
# model.apply(init_gaussian)

# Pour tester Constant :
# model.apply(init_constant)

# ==============================
# 10. PARAMÈTRES DU MODÈLE
# ==============================
print("\n===== PARAMÈTRES DU MODÈLE =====")

for name, param in model.named_parameters():
    print(name, param.shape)

print("\n===== STATE DICT =====")
print(model.state_dict().keys())

# ==============================
# 11. LOSS + OPTIMIZER
# ==============================
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# ==============================
# 12. ENTRAÎNEMENT
# ==============================
print("\n===== ENTRAÎNEMENT =====")

for epoch in range(50):

    outputs = model(X_train)

    loss = criterion(outputs, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch} | Loss : {loss.item()}")

# ==============================
# 13. TEST
# ==============================
with torch.no_grad():

    outputs = model(X_test)

    _, predicted = torch.max(outputs, 1)

# ==============================
# 14. MÉTRIQUES
# ==============================
y_true = y_test.cpu().numpy()
y_pred = predicted.cpu().numpy()

accuracy = accuracy_score(y_true, y_pred)

precision = precision_score(y_true, y_pred)

recall = recall_score(y_true, y_pred)

f1 = f1_score(y_true, y_pred)

conf_matrix = confusion_matrix(y_true, y_pred)

# ==============================
# 15. AFFICHAGE RÉSULTATS
# ==============================
print("\n===== RÉSULTATS =====")

print("Accuracy        :", accuracy)

print("Precision       :", precision)

print("Recall          :", recall)

print("F1-score        :", f1)

print("Confusion Matrix:\n", conf_matrix)

# ==============================
# 16. SAUVEGARDE MODÈLE
# ==============================
torch.save(
    model.state_dict(),
    "mlp_model.pth"
)

print("\nModèle sauvegardé avec succès !")

# ==============================
# 17. RECHARGEMENT MODÈLE
# ==============================
new_model = MonMLP().to(device)

new_model.load_state_dict(
    torch.load("mlp_model.pth")
)

new_model.eval()

print("Modèle rechargé avec succès !")

print("\n===== NAMED PARAMETERS =====")

for name, param in model.named_parameters():
    print(name, param.shape)

print("\n===== STATE DICT =====")

for key in model.state_dict():
    print(key)