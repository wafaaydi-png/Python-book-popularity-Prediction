## 📚 Prédiction de la Popularité des Livres | Machine Learning & Flask

## 📌 Présentation du projet

Ce projet consiste en la création d’un **modèle de Machine Learning** capable de prédire la popularité d’un livre à partir de différentes informations textuelles et numériques, ainsi qu’au développement d’une **application web interactive avec Flask** permettant d’effectuer des prédictions en temps réel.

L’objectif est de construire un pipeline complet allant de la préparation des données jusqu’au déploiement du modèle, afin de transformer les données littéraires en **prédictions exploitables** sur le succès potentiel d’un livre.

---

# 📂 Structure du projet

## 1️⃣ Préparation et analyse des données

Cette étape est dédiée au nettoyage, à la transformation et à l’enrichissement du dataset avant l’entraînement des modèles.

### Traitements réalisés

- Nettoyage des données
- Suppression des doublons
- Gestion des valeurs manquantes
- Préparation des variables cibles

### Feature engineering

- Extraction du nombre d’avis utiles
- Extraction du nombre total d’avis
- Calcul du pourcentage d’avis utiles
- Fusion des variables textuelles

### Variables utilisées

- Titre du livre
- Prix
- Résumé de l’avis
- Texte complet de l’avis
- Description du livre
- Auteurs
- Catégories
- Nombre d’avis utiles
- Nombre total d’avis

### Objectif

Préparer un jeu de données propre et pertinent pour optimiser les performances du modèle prédictif.

---

## 2️⃣ Modélisation Machine Learning

Cette étape permet d’entraîner et de comparer plusieurs modèles de classification afin de sélectionner le plus performant.

### Modèles testés

- Régression Logistique
- Random Forest
- Gradient Boosting
- Naive Bayes
- XGBoost

### Méthodes utilisées

- Vectorisation du texte avec TF-IDF
- Pipeline de prétraitement automatisé
- Entraînement et validation des modèles
- Comparaison des performances

### Meilleur modèle sélectionné

- Régression Logistique avec TF-IDF

### Performance du modèle

- Accuracy : 70,5 %
- F1 Score pondéré : 70,7 %
- Évaluation ROC-AUC

### Objectif

Construire un modèle fiable capable de prédire si un livre sera populaire ou non.

---

## 3️⃣ Application web Flask

Cette partie permet d’intégrer le modèle entraîné dans une interface web interactive pour réaliser des prédictions en temps réel.

### Fonctionnalités disponibles

- Saisie des informations du livre
- Prétraitement automatique des données
- Prédiction instantanée
- Affichage du résultat :
  - Populaire
  - Non populaire

### Fichiers du projet

- `book_popularity_ml_clean_notebook_with_models.ipynb`
- `app.py`
- `book_popularity_model.pkl`
- `index.html`

### Objectif

Rendre le modèle accessible via une interface simple et intuitive.

---

# 🛠️ Outils utilisés

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Joblib
- Flask
- HTML / CSS

---

# 🎯 Résultats attendus

Ce projet permet de :

- Nettoyer et préparer des données textuelles complexes
- Construire un pipeline complet de Machine Learning
- Comparer plusieurs modèles de classification
- Déployer un modèle prédictif dans une application web
- Réaliser des prédictions interactives sur la popularité des livres
