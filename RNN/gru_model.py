# ==============================
# 1. IMPORTS
# ==============================
import torch
import torch.nn as nn
import torch.optim as optim

from datasets import load_dataset
from collections import Counter

# ==============================
# 2. DEVICE
# ==============================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Device utilisé :", device)

# ==============================
# 3. CHARGER DATASET
# ==============================
dataset = load_dataset("imdb")

# ==============================
# 4. PETIT SOUS-ENSEMBLE
# ==============================
texts = []
labels = []

for i in range(200):

    text = dataset["train"][i]["text"].lower().split()

    texts.append(text[:50])

    labels.append(dataset["train"][i]["label"])

# ==============================
# 5. VOCABULAIRE
# ==============================
all_words = []

for text in texts:
    all_words.extend(text)

counter = Counter(all_words)

vocab = {
    "<PAD>": 0,
    "<UNK>": 1
}

for idx, word in enumerate(counter.keys()):
    vocab[word] = idx + 2
encoded = [
    vocab.get(word, vocab["<UNK>"])
    for word in text
]

vocab_size = len(vocab) + 1

print("Vocab size :", vocab_size)

# ==============================
# 6. ENCODAGE
# ==============================
encoded_texts = []

for text in texts:

    encoded = [vocab[word] for word in text]

    while len(encoded) < 50:
        encoded.append(0)

    encoded_texts.append(encoded)

# ==============================
# 7. TENSEURS
# ==============================
X = torch.tensor(encoded_texts).to(device)

y = torch.tensor(labels).to(device)

print("Shape X :", X.shape)

# ==============================
# 8. MODÈLE GRU
# ==============================
class SimpleGRU(nn.Module):

    def __init__(self):

        super(SimpleGRU, self).__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size,
            embedding_dim=32
        )

        self.gru = nn.GRU(
            input_size=32,
            hidden_size=64,
            batch_first=True
        )

        self.fc = nn.Linear(64, 2)

    def forward(self, x):

        x = self.embedding(x)

        output, hidden = self.gru(x)

        hidden = hidden[-1]

        x = self.fc(hidden)

        return x

# ==============================
# 9. MODÈLE
# ==============================
model = SimpleGRU().to(device)

print(model)

# ==============================
# 10. LOSS + OPTIMIZER
# ==============================
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# ==============================
# 11. ENTRAÎNEMENT
# ==============================
print("\n===== ENTRAÎNEMENT GRU =====")

for epoch in range(5):

    outputs = model(X)

    loss = criterion(outputs, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# ==============================
# 12. PRÉDICTIONS
# ==============================
with torch.no_grad():

    outputs = model(X)

    _, predicted = torch.max(outputs, 1)

accuracy = (predicted == y).sum().item() / len(y)

print("\nAccuracy GRU :", accuracy)