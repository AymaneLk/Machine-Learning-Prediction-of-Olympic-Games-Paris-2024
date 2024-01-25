# Introduction 
La prédiction des événements sportifs, tels que les Jeux Olympiques, est complexe et incertaine. 
Bien que le passé offre des indices, les sports évoluent et des facteurs imprévus, comme les conditions météorologiques ou les états psychologiques des athlètes, peuvent influencer les résultats. 
Les caractéristiques sélectionnées pour les modèles prédictifs enrichissent l'analyse, mais leur précision dépend de leur pertinence et qualité. 
Il est crucial de traiter les prévisions de machine learning comme des guides plutôt que des garanties absolues, en tenant compte de l'élément d'incertitude inhérent à de tels événements.

# Source :
    Kaggle
    Choix d'un jeu de données très large (1896-2022) pour avoir un large éventail de données par pays.
    https://www.kaggle.com/datasets/piterfm/olympic-games-medals-19862018?select=olympic_medals.csv

# Etapes réalisées :

**1- Récupération des fichiers à partir de Kaggle**

**2 - Transformation des données
Récupération des fichiers sur Kaggle.
Supression des colones inutiles (url  athlète, coutry code 3 letter, country code 2 letter...)dans l'objectif de réduire la lourdeur des fichiers suite à la répétition de données ou à la supression de celles inutiles**

**3 - Importation des datas sur MariaDB à partir d'un script Python `insert_data_to_db.py`.**

# Installation

**1 - Ouvrir docker**\

**2 - Lancer le fichier `docker-compose.yaml`**\

**3 - Lancer les commandes :**\
`python3 -m venv venv` \
`source venv/bin/activate`\
`pip install -r requirements.txt`\
    
**4 - Lancer le script Python de creation de BDD et d'insertion de données.**
