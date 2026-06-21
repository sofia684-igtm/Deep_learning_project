import matplotlib.pyplot as plt

labels = ["Malignant", "Benign"]
sizes = [212, 357]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Breast Cancer Class Distribution")
plt.show()