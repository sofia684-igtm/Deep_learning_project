import torch
import torch.nn as nn

# ==========================
# VOCABULAIRE MINIATURE
# ==========================

input_vocab_size = 10
output_vocab_size = 10

# ==========================
# ENCODEUR
# ==========================

class Encoder(nn.Module):

    def __init__(self):

        super().__init__()

        self.embedding = nn.Embedding(
            input_vocab_size,
            8
        )

        self.lstm = nn.LSTM(
            8,
            16,
            batch_first=True
        )

    def forward(self, x):

        x = self.embedding(x)

        outputs, (hidden, cell) = self.lstm(x)

        return hidden, cell


# ==========================
# DÉCODEUR
# ==========================

class Decoder(nn.Module):

    def __init__(self):

        super().__init__()

        self.embedding = nn.Embedding(
            output_vocab_size,
            8
        )

        self.lstm = nn.LSTM(
            8,
            16,
            batch_first=True
        )

        self.fc = nn.Linear(
            16,
            output_vocab_size
        )

    def forward(
        self,
        x,
        hidden,
        cell
    ):

        x = self.embedding(x)

        output, (hidden, cell) = self.lstm(
            x,
            (hidden, cell)
        )

        prediction = self.fc(output)

        return prediction, hidden, cell


# ==========================
# SEQ2SEQ
# ==========================

class Seq2Seq(nn.Module):

    def __init__(
        self,
        encoder,
        decoder
    ):

        super().__init__()

        self.encoder = encoder
        self.decoder = decoder

    def forward(
        self,
        source,
        target
    ):

        hidden, cell = self.encoder(source)

        outputs = []

        decoder_input = target[:, 0].unsqueeze(1)

        for t in range(
            target.shape[1]
        ):

            output, hidden, cell = self.decoder(
                decoder_input,
                hidden,
                cell
            )

            outputs.append(output)

            decoder_input = output.argmax(
                dim=2
            )

        return torch.cat(outputs, dim=1)


# ==========================
# TEST
# ==========================

encoder = Encoder()

decoder = Decoder()

model = Seq2Seq(
    encoder,
    decoder
)

source = torch.randint(
    0,
    10,
    (2, 5)
)

target = torch.randint(
    0,
    10,
    (2, 5)
)

output = model(
    source,
    target
)
criterion = nn.CrossEntropyLoss()

loss = criterion(
    output.reshape(-1, output_vocab_size),
    target.reshape(-1)
)

print("Loss :", loss.item())

perplexity = torch.exp(loss)

print("Perplexity :", perplexity.item())

print(model)

print(
    "\nOutput shape :",
    output.shape
)
# ==========================
# GREEDY DECODING
# ==========================

print("\n===== GREEDY DECODING =====")

predictions = output.argmax(dim=2)
print("\n===== BEAM SEARCH =====")
beam_width = 3

probs = torch.softmax(
    output,
    dim=2
)

top_probs, top_tokens = torch.topk(
    probs,
    beam_width,
    dim=2
)

print("Top tokens :")
print(top_tokens)

print("\nTop probabilities :")
print(top_probs)

print("Source :")
print(source)

print("\nTarget :")
print(target)

print("\nPredictions :")
print(predictions)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

optimizer.zero_grad()

output = model(
    source,
    target
)

loss = criterion(
    output.reshape(-1, output_vocab_size),
    target.reshape(-1)
)

loss.backward()

# Norme avant clipping

total_norm = 0

for p in model.parameters():

    if p.grad is not None:

        param_norm = p.grad.data.norm(2)

        total_norm += param_norm.item() ** 2

total_norm = total_norm ** 0.5

print(
    "Gradient norm before clipping:",
    total_norm
)

# Clipping

torch.nn.utils.clip_grad_norm_(
    model.parameters(),
    max_norm=1.0
)

# Norme après clipping

clipped_norm = 0

for p in model.parameters():

    if p.grad is not None:

        param_norm = p.grad.data.norm(2)

        clipped_norm += param_norm.item() ** 2

clipped_norm = clipped_norm ** 0.5

print(
    "Gradient norm after clipping:",
    clipped_norm
)

optimizer.step()
