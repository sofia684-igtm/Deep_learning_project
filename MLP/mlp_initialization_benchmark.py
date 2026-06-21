import matplotlib.pyplot as plt

methods = [
    "Xavier",
    "Gaussian",
    "Constant"
]

acc = [
    84.21,
    62.28,
    94.74
]

plt.figure(figsize=(8,5))

plt.bar(methods, acc)

plt.ylabel("Accuracy (%)")
plt.title("Comparison of Weight Initializations")

plt.show()