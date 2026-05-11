# 📚 Prédiction de la Popularité des Livres - Machine Learning & Flask

## 📌 Description du projet
Ce projet permet de **prédire la popularité d’un livre** à l’aide du **Machine Learning** et d’une **application web Flask**.

Le modèle prédit si un livre sera :

- ✅ **Populaire**
- ❌ **Non populaire**

à partir de plusieurs informations fournies sur le livre :

- Titre du livre
- Prix
- Résumé de l’avis
- Texte complet de l’avis
- Description du livre
- Nombre d’avis utiles
- Nombre total d’avis

Le résultat est affiché dans une interface web interactive.

---

## 🎯 Objectif du projet
Construire un pipeline complet de Machine Learning permettant de :

- nettoyer et préparer les données
- transformer les données textuelles et numériques
- entraîner plusieurs modèles de classification
- comparer leurs performances
- sélectionner le meilleur modèle
- sauvegarder le modèle final
- intégrer le modèle dans une application Flask

---

## 📂 Fichiers du projet

- `book_popularity_ml_clean_notebook_with_models.ipynb`  
  → Notebook complet d’analyse et d’entraînement du modèle

- `app.py`  
  → Application Flask pour effectuer la prédiction

- `book_popularity_model.pkl`  
  → Modèle entraîné sauvegardé

- `index.html`  
  → Interface utilisateur de prédiction

---

## 📊 Informations sur le dataset

Le jeu de données contient **15 719 livres** avec les variables suivantes :

- `title` → titre
- `price` → prix
- `review/helpfulness` → utilité des avis
- `review/summary` → résumé de l’avis
- `review/text` → texte de l’avis
- `description` → description du livre
- `authors` → auteurs
- `categories` → catégories
- `popularity` → popularité (variable cible)

---

## ⚙️ Préparation des données

### Nettoyage des données
- Suppression des doublons
- Suppression des valeurs manquantes sur la variable cible

### Création de nouvelles variables
À partir de `review/helpfulness`, création de :

- `num_helpful` → nombre d’avis utiles
- `num_reviews` → nombre total de votes
- `perc_helpful_reviews` → pourcentage d’avis utiles

### Traitement du texte
Fusion des colonnes textuelles dans une seule variable :

- titre
- auteurs
- catégories
- résumé
- texte de l’avis
- description

Transformation du texte avec **TF-IDF Vectorizer**.

---

## 🤖 Modèles de Machine Learning testés

Plusieurs modèles ont été comparés :

- Régression Logistique + TF-IDF
- Random Forest
- Gradient Boosting
- Naive Bayes
- XGBoost (optionnel)

### Meilleur modèle sélectionné

✅ **Régression Logistique + TF-IDF**

### Performances

- Accuracy : **70,5 %**
- F1 Score pondéré : **70,7 %**
- ROC-AUC évalué

---

## 💾 Sauvegarde du modèle

Le pipeline complet a été sauvegardé avec **joblib** :

- `book_popularity_model.pkl`

Cela permet à Flask d’utiliser exactement le même prétraitement et le même modèle pour la prédiction.

---

## 🌐 Application Flask

L’utilisateur peut saisir :

- Titre du livre
- Prix
- Résumé de l’avis
- Texte complet de l’avis
- Description
- Nombre d’avis utiles
- Nombre total d’avis

Puis cliquer sur **Prédire** pour obtenir :

- **Populaire**
- **Non populaire**

---
## Capture d'écran
![capture]("b5.png")

## 🛠️ Technologies utilisées

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Joblib
- Flask
- HTML / CSS

---

