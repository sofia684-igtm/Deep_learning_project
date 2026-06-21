# Deep Learning Project

Petit projet d'apprentissage profond contenant des exemples MLP, RNN et CNN et une interface Streamlit.

## Structure

- `app.py` — point d'entrée Streamlit
- `CNN/`, `MLP/`, `RNN/` — scripts d'exemples et modèles
- `data/MNIST/raw` — jeux de données (non committés)
- `requirements_streamlit.txt` — dépendances pour exécuter l'interface

## Prérequis

- Python 3.8+
- Créer un environnement virtuel (recommandé)

## Installation

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements_streamlit.txt
```

Copiez ou placez les données MNIST dans `data/MNIST/raw` si vous souhaitez exécuter les notebooks/scripts qui en dépendent.

## Lancer l'interface Streamlit

```bash
streamlit run app.py
```

## Notes

- Les fichiers volumineux et les modèles entraînés sont exclus via `.gitignore`.
- Voir le dossier `report/` pour le rapport final.

---
Repository poussé sur GitHub: https://github.com/sofia684-igtm/Deep_learning_project.git
