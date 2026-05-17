## ELT Pipeline
    -  S3
    -  dbt 
    -  Analytics API
    
Projet simple de data engineering qui permet de transformer des données brutes en analyses exploitables.

---

## Objectif

Construire un pipeline data complet :

- ingestion des données
- transformation
- modélisation
- visualisation

---

## Architecture

- **storage/** → stockage des données (ex: S3)
- **dbt/** → transformations SQL
- **src/** → code Python (API, scripts)
- **notebooks/** → analyse exploratoire
- **powerbi/** → dashboards et visualisation

---

## Pipeline

raw data → dbt staging → dbt marts → PostgreSQL → Power BI

---

## dbt

Outil de transformation des données.

- **staging** : nettoyage et préparation
- **marts** : KPI et modèles analytiques

### Commandes principales

```bash
dbt run
dbt test
dbt docs generate
dbt docs serve --host 0.0.0.0 --port 8080
```

### Power BI

Outil de visualisation utilisé pour :

- analyser les ventes
- suivre les KPI
- créer des dashboards

---

### Résultat attendu

Un système complet permettant de :

- collecter des données
- les transformer avec dbt
- les stocker dans PostgreSQL
- les visualiser avec Power BI
