# Projet : Contamination des sols a la chlordecone en Martinique

**ENSAR — A1 Data Science — 2025-2026**  
**Cours : Ingenierie des donnees — S. Manou-Abi**

## Description

La chlordecone est un pesticide organochloré utilisé aux Antilles francaises jusqu'au debut des annees 1990. Ce projet exploite le dataset `BaseCLD2026.csv` (31 126 observations, ~3 600 parcelles uniques) pour structurer, nettoyer et analyser les donnees de contamination en Martinique.

## Structure du depot

```
├── README.md
├── requirements.txt
├── notebooks/
│   ├── projet_chlordecone.ipynb
│   └── projet_chlordecone.Rmd
├── data/
│   └── BaseCLD2026.csv
├── docs/
│   └── Dictionnaire_Parcelles_Chlordecone.docx
├── figures/
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
cd notebooks
jupyter notebook projet_chlordecone.ipynb
```

## Donnees

Chaque ligne = un point raster dans une parcelle. Une parcelle (ID) a plusieurs lignes avec le meme taux CLD mais des variables topographiques differentes. Les tests statistiques sont faits sur donnees agregees par parcelle pour eviter la pseudo-replication.

## Contenu

**Volet 1 — Ingenierie** : manipulation tabulaire, recodage, jointures, flux de controle, dates, text mining, valeurs manquantes (imputation + test KS), donnees spatiales

**Volet 2 — Analyse** : EDA, ACP (formules du cours), AFC, K-means, CAH, KNN, tests statistiques (ANOVA, Chi2, Spearman, Kruskal-Wallis, Shapiro-Wilk), aide a la decision

## Resultats

1. Contamination tres heterogene (mediane 150x plus faible que la moyenne)
2. Les Andosols retiennent davantage la chlordecone (ANOVA significative)
3. Zones de forte pluviometrie plus contaminees
4. Profils territoriaux distincts identifies par clustering

## Auteur

Younes Ouloum — ENSAR A1 SD
