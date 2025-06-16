# 🔧 Projet de test SOAP automatisé

## 🎯 Objectif
Automatiser les tests d’un service SOAP (exemple : conversion de nombre) pour s’entraîner à la mise en place d’une CI/CD avant d’avoir accès à POWERCARDCONNECTAPI.

---

## ▶️ Lancer les tests en local

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
pytest test_soap_client.py --junitxml=results.xml --html=report.html
