import torch
import torch.nn as nn
import torch.optim as optim

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

# =====================================
# DATASET
# =====================================

data = load_breast_cancer()

X = data.data
y = data.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)

y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)

# =====================================
# MLP
# =====================================

class MLP(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(30, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 2)
        )

    def forward(self, x):
        return self.network(x)

# =====================================
# INITIALISATIONS
# =====================================

def init_xavier(model):
    for m in model.modules():
        if isinstance(m, nn.Linear):
            nn.init.xavier_uniform_(m.weight)

def init_gaussian(model):
    for m in model.modules():
        if isinstance(m, nn.Linear):
            nn.init.normal_(m.weight, mean=0, std=0.01)

def init_constant(model):
    for m in model.modules():
        if isinstance(m, nn.Linear):
            nn.init.constant_(m.weight, 0.5)

# =====================================
# ENTRAINEMENT
# =====================================

def train_and_evaluate(init_function, name):

    model = MLP()

    init_function(model)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(
        model.parameters(),
        lr=0.001
    )

    for epoch in range(50):

        outputs = model(X_train)

        loss = criterion(outputs, y_train)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

    with torch.no_grad():

        predictions = model(X_test)

        predicted = torch.argmax(
            predictions,
            dim=1
        )

    y_true = y_test.numpy()
    y_pred = predicted.numpy()

    print("\n======================")
    print(name)
    print("======================")

    print(
        "Accuracy :",
        accuracy_score(y_true, y_pred)
    )

    print(
        "Precision :",
        precision_score(y_true, y_pred)
    )

    print(
        "Recall :",
        recall_score(y_true, y_pred)
    )

    print(
        "F1-score :",
        f1_score(y_true, y_pred)
    )

    print(
        "\nConfusion Matrix :"
    )

    print(
        confusion_matrix(
            y_true,
            y_pred
        )
    )

# =====================================
# TESTS
# =====================================

train_and_evaluate(
    init_xavier,
    "XAVIER"
)

train_and_evaluate(
    init_gaussian,
    "GAUSSIAN"
)

train_and_evaluate(
    init_constant,
    "CONSTANT"
)