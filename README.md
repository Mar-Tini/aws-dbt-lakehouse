## ELT Pipeline
    -  S3
    -  dbt 
    -  Analytics API


## DBT Documentation Server

Pour générer et lancer la documentation du projet dbt :

### 1. Générer la documentation

    dbt docs generate

### 2. Lancer le serveur de documentation

    dbt docs serve --host 0.0.0.0 --port 8080

### 3. Accéder à l’interface

    http://localhost:8080