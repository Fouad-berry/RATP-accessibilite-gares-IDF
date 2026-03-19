# 🚉 Analyse de l’accessibilité des gares en Île-de-France

## 📌 Objectif du projet

Ce projet vise à analyser le niveau d’accessibilité des gares en Île-de-France à partir de données ouvertes fournies par Île-de-France Mobilités.

L’objectif est de :

* Identifier les gares non accessibles
* Comprendre la répartition de l’accessibilité
* Visualiser les zones problématiques
* Fournir un dashboard interactif avec Power BI

---

## 📊 Données utilisées

* Source : Île-de-France Mobilités (Open Data)
* Formats :

  * CSV (analyse)
  * GEOJSON (visualisation géographique)

---

## 🧰 Stack technique

* Python (pandas)
* Power BI
* Jupyter Notebook

---

## 🏗️ Structure du projet

```
accessibilite-gares-idf/
│
├── data/
│   ├── raw/            # Données brutes
│   └── processed/      # Données nettoyées
│
├── notebooks/          # Analyse exploratoire (EDA)
├── scripts/            # Scripts Python
├── powerbi/            # Dashboard Power BI (.pbix)
├── images/             # Screenshots du dashboard
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Exécution

### 1. Nettoyage des données

```bash
python3 scripts/data_cleaning.py
```

### 2. Analyse des données

```bash
python3 scripts/analysis.py
```

---

## 📈 Dashboard Power BI


Le fichier Power BI (.pbix) se trouve dans le dossier `powerbi/` du projet, si vous souhaitez l'ouvrir ou l'explorer directement dans Power BI.

Le dashboard permet de visualiser :

* 📍 Carte des gares avec niveau d’accessibilité
* 📊 Nombre de gares par niveau d’accessibilité
* 🥧 Répartition (%) des niveaux d’accessibilité
* 📋 Liste des gares non accessibles
* 🎯 Indicateurs clés (KPI)

---

## 🔍 Insights clés

* Une part significative des gares reste **non accessible**, ce qui met en évidence un enjeu d’inclusion important.
* Les gares accessibles en totale autonomie sont **minoritaire** par rapport aux autres catégories.
* L’accessibilité est **inégale selon les zones**, avec une forte concentration autour de Paris.
* Les gares nécessitant une assistance (sur demande ou réservation) représentent une part importante du réseau.
* Le dashboard permet d’identifier rapidement les **zones prioritaires d’amélioration**.

---

## 💡 Améliorations possibles

* Simplification des niveaux d’accessibilité (Accessible / Partiel / Non accessible)
* Ajout d’un score d’accessibilité
* Analyse temporelle (si données historiques)
* Intégration d’une API pour données en temps réel

---

## 💼 Compétences mises en œuvre

* Data cleaning (pandas)
* Analyse exploratoire de données (EDA)
* Data visualisation (Power BI)
* Manipulation de données géographiques
* Structuration d’un projet data

---

## 🎯 Conclusion

Ce projet met en évidence les enjeux d’accessibilité dans les transports publics en Île-de-France et démontre la capacité à transformer des données brutes en insights exploitables via un dashboard interactif.

---

## 🖼️ Aperçu du dashboard

![Dashboard](images/dashboard.jpg)
