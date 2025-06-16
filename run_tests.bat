@echo off
REM Création de l’environnement virtuel Python
C:\Users\allo\AppData\Local\Programs\Python\Python313\python.exe -m venv venv

REM Activation de l’environnement et installation des dépendances
venv\Scripts\pip install --upgrade pip
venv\Scripts\pip install -r requirements.txt

REM Lancement des tests avec génération des rapports
venv\Scripts\pytest test_soap_client.py --junitxml=results.xml --html=report.html
