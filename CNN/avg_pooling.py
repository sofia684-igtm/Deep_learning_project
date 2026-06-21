import torch

def avg_pool2d(X, pool_size):

    p_h, p_w = pool_size

    Y = torch.zeros(
        (
            X.shape[0] - p_h + 1,
            X.shape[1] - p_w + 1
        )
    )

    for i in range(Y.shape[0]):
        for j in range(Y.shape[1]):

            Y[i, j] = torch.mean(
                X[i:i+p_h, j:j+p_w]
            )

    return Y


X = torch.tensor([
    [0., 1., 2.],
    [3., 4., 5.],
    [6., 7., 8.]
])

print("Input :")
print(X)

print("\nAverage Pooling Output :")
print(
    avg_pool2d(
        X,
        (2, 2)
    )
)