import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

import numpy as np

cm = np.array([
    [41, 2],
    [4, 67]
])

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Malignant", "Benign"]
)

disp.plot(cmap="Blues")

plt.title("MLP Confusion Matrix")
plt.show()