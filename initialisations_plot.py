import matplotlib.pyplot as plt

# Résultats obtenus
initialisations = ["Gaussian", "Xavier", "Constant"]
accuracies = [62.28, 84.21, 94.74]

plt.figure(figsize=(8, 5))

plt.bar(initialisations, accuracies)

plt.title("Comparaison des méthodes d'initialisation des poids")
plt.xlabel("Méthode d'initialisation")
plt.ylabel("Accuracy (%)")

plt.ylim(0, 100)

for i, acc in enumerate(accuracies):
    plt.text(i, acc + 1, f"{acc}%", ha="center")

plt.tight_layout()

plt.savefig("figure_6_initialisations.png", dpi=300)

plt.show()