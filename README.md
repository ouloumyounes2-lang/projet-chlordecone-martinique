# 🧪 Analyse et Ingénierie des Données de la Chlordécone aux Antilles françaises

**ENSAR — École Nationale Supérieure d'Arts et Réseaux, Niort**  
**Parcours A1 Data Science — 2025-2026**  
**Cours : Ingénierie des données avec Python et RStudio — S. Manou-Abi**

---

## 📋 Description du projet

La **chlordécone** est un pesticide organochloré utilisé aux Antilles françaises jusqu'au début des années 1990. Sa persistance dans les sols, les eaux et les chaînes alimentaires en fait un enjeu sanitaire, environnemental et socio-économique majeur.

Ce projet exploite le dataset `BaseCLD2026.csv` (31 126 observations, 22 variables) pour :
- **Structurer, nettoyer et transformer** les données (pipeline reproductible)
- **Mener des analyses statistiques** exploratoires et multivariées
- **Produire des insights** utiles à la prise de décision publique

---

## 📁 Structure du dépôt

```
├── README.md                          # Ce fichier
├── projet_chlordecone.ipynb           # Notebook Python (Jupyter) — COMPLET
├── projet_chlordecone.Rmd             # R Markdown — COMPLET
├── BaseCLD2026.csv                    # Dataset principal
├── Dictionnaire_Parcelles.docx        # Dictionnaire des données
├── figures/
│   ├── missing_values.png
│   ├── carte_contamination.png
│   ├── carte_communes.png
│   ├── eda_dashboard.png
│   ├── multivarie.png
│   ├── acp.png
│   ├── afc.png
│   ├── elbow.png
│   ├── kmeans.png
│   ├── dendrogramme.png
│   ├── knn_k_optimal.png
│   ├── knn_confusion.png
│   └── aide_decision.png
```

---

## 📊 Données

| Variable | Description |
|----------|------------|
| `ID` | Identifiant unique de la parcelle |
| `ANNEE` | Année d'observation (2010–2019) |
| `COMMU_LAB` | Commune (35 communes martiniquaises) |
| `RAIN` | Groupe de pluviométrie |
| `Sol_simple` | Type de sol simplifié (Andosol, Ferralsol, Nitisol...) |
| `type_sol` | Classification détaillée du sol |
| `Date_prelevement` | Date de prélèvement |
| `Taux_Chlordecone` | Taux mesuré de chlordécone (mg/kg) |
| `Operateur_chld` | `=` (détecté) ou `<` (sous seuil de détection) |
| `Taux_5b_hydro` | Taux de 5b-hydro chlordécone |
| `histoBanane_Histo_ban` | Historique bananier (1=jamais, 2=passé, 3=actuel) |
| `mnt_*` | Variables topographiques (pente, rugosité, exposition...) |
| `X`, `Y` | Coordonnées géographiques projetées |

---

## 🔧 Volet 1 — Ingénierie des Données

| Compétence | Démonstration |
|-----------|--------------|
| `group_by` / `summarise` | Agrégation par commune, sol, année |
| `filter` / `mutate` | Filtrage multi-critères, création de variables dérivées |
| Détection d'incohérences | Dates 9999, valeurs "inf"/"999", "Hors Martinique" |
| Recodage | Pluviométrie, historique bananier, classes de contamination |
| Jointures | LEFT, RIGHT, INNER, FULL + analyse d'impact |
| Flux de contrôle | if/else, switch, for, while, apply/sapply |
| Dates | Conversion, extraction année/mois/trimestre/saison, délais |
| Text Mining | Tokenisation de `type_sol`, extraction de mots-clés |
| Valeurs manquantes | Identification, visualisation, imputation (mode, médiane, KNN spatial) |
| Pipeline reproductible | Fonction `pipeline_nettoyage()` documentée |
| Données spatiales | Cartographie, agrégation géographique par commune |

---

## 📈 Volet 2 — Analyse de Données

| Méthode | Résultat clé |
|---------|-------------|
| **EDA** | Distribution très asymétrique, forte hétérogénéité spatiale |
| **ACP** | Les variables topographiques (pente, rugosité, TRI) forment un axe majeur |
| **AFC** | Association significative Sol × Contamination (Chi² p < 0.001) |
| **K-Means** | Profils territoriaux distincts identifiés |
| **CAH** | Dendrogramme confirme 3-4 groupes naturels |
| **KNN** | Classification des niveaux de contamination par le terrain |
| **ANOVA** | Différence significative du taux selon le type de sol |
| **Kruskal-Wallis** | Effet significatif de la pluviométrie |
| **Spearman** | Corrélation taux-pente significative |

---

## 🎯 Résultats et Recommandations

### Résultats clés
1. **Contamination hétérogène** : la médiane (0.0033 mg/kg) est très inférieure à la moyenne (0.67 mg/kg), indiquant que quelques parcelles concentrent l'essentiel de la pollution
2. **Facteurs de risque** : Andosols, historique bananier, forte pluviométrie
3. **Zones critiques** identifiées par le clustering et l'analyse spatiale

### Recommandations
- Prioriser la surveillance sur les communes identifiées comme zones critiques
- Adapter les pratiques agricoles selon le type de sol (Andosol = plus rétenteur)
- Renforcer le suivi des zones de forte pluviométrie
- Améliorer la collecte de données (58% de NaN sur l'historique bananier)

---

## 🛠️ Technologies

- **Python** : pandas, numpy, scikit-learn, matplotlib, seaborn, scipy
- **R** : dplyr, ggplot2, FactoMineR, factoextra, lubridate, corrplot
- **Git** : versionnement du projet

---

## 👤 Auteur

**Younes** — ENSAR A1 SD, 2025-2026
