# MERGE SUR MAIN LE TAFF
# Participants
## Theron Benjamin && Lkhawa Ayman 

### Sources (question 1) :
    Kaggle
    Choix d'un jeu de données très large (1896-2022) suite aux questions demandées et pour avoir un large éventail de données par pays.
    https://www.kaggle.com/datasets/piterfm/olympic-games-medals-19862018?select=olympic_medals.csv

# Etapes que nous avons réalisées :

## 1- Récupération des fichiers à partir de kaggle

## 2 - Transformation des données
    récupération des fichiers sur kaggle 
    supression des colones inutiles (url  athlète, coutry code 3 letter, country code 2 letter...) 
    dans l'objectif de réduire la lourdeur des fichiers suite à la répétition de données ou à la supression de celles inutiles
## 3 - Importation des datas sur maria DB à partir d'un script python

# Installation

## 1 - ouvrir docker
## 2 - lancer le fichier docker-compose.yaml
## 3 - lancer les commandes :
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
## 3 - lancer le script python de creation de BDD et d'insertion de données

### QUESTIONS 

## 2
    1 - ouvrir le notebook dans notebook/olympic_games.ipynb
    2 - lancer les script 1 par 1
    3 - visualiser les résultats

## 3 - Pouvez-vous prédire les pays médaillés dans au moins 2 disciplines lors des JO de Paris ?
    1 - ouvrir le notebook dans notebook/paris_olympics.ipynb
    2 - lancer les script 1 par 1
    3 - visualiser les résultats

## 4 - Pouvez-vous prédire les athlètes médaillés dans au moins 2 disciplines lors des JO de Paris ?
    1 - ouvrir le notebook dans notebook/paris_olympics.ipynb
    2 - lancer les script 1 par 1
    3 - visualiser les résultats

## 5 - Pouvez-vous prédire le nombre total de médailles françaises lors des JO de Paris ?
    1 - ouvrir le notebook dans notebook/paris_olympics.ipynb
    2 - lancer les script 1 par 1
    3 - visualiser les résultats

## 6 - Que pensez-vous de cet article ? https://drive.google.com/file/d/1SZQBHHFpucBf3VdmNn_ceuisHGdsklba/view
    Context : Dans l'étude "Forecasting the Olympic medal distribution during a pandemic", un modèle d'apprentissage automatique à deux étages prédit les médailles olympiques par nation, surpassant les méthodes traditionnelles pour les Jeux de 2008 à 2016.
    Cet article nous démontre que de nombreux facteurs sont à rendre en compte dans la réalisation de prévisions/prédictions.
    Certains de ces facteurs sont diffcilement prévisibles à l'avance. La pandémie est un exemple qui a bouleversé la routine des sportifs quand à leur préparation.
    L'isolation, le non-accès à des structures décentes, la solitude... sont des ressentis propres à chaque humain et, difficilement quantifiables.
    Ces paramètres représentent généralement un risque plutôt qu'une opportunité.
    Cette approche est extrêmement intéressante et, démontre bien que l'évaluation des données peut-être très poussée et complexe.
    Ici, le model présenté intègre des données telles que le PIB et la santé publique, reflétant l'impact du COVID-19 sur les performances sportives. 
    De notre point de vue, la généralisation de facteur personnel et de leur quantification offre une perspective plus précise sur les résultats potentiels.

## 7 - Quelles conclusions tirez-vous de votre étude des JO par les données ? Pouvez-vous parier les yeux fermés avec vos résultats ?
    La prédiction des événements sportifs, tels que les Jeux Olympiques, est complexe et incertaine. 
    Bien que le passé offre des indices, les sports évoluent et des facteurs imprévus, comme les conditions météorologiques ou les états psychologiques des athlètes, peuvent influencer les résultats. 
    Les caractéristiques sélectionnées pour les modèles prédictifs enrichissent l'analyse, mais leur précision dépend de leur pertinence et qualité. 
    Il est crucial de traiter les prévisions de machine learning comme des guides plutôt que des garanties absolues, en tenant compte de l'élément d'incertitude inhérent à de tels événements.
    Suite à nos résultats, nous sommes tout de même prêt pour parier une petite mise. 
    En effet, nous avons vérifier l'historique sur google concernant ceux-ci est cela semble cohérent.

## 8 - Avez-vous besoin du Big Data pour ce projet ?
    Il ne fut pas nécessaire d'utiliser le Big Data concernant la partie 2.
    Les fichiers récupérés étant bien découpé et le fait de ne pas avoir besoin de regrouper
    les informations à partir différentes tables nous ont permis d'aller vite avec des requêtes basiques.
    Dans un cas plus complexe, nous aurions utilisé Spark





