import subprocess
import requests

# Lancer l'API FastAPI en arrière-plan
api_process = subprocess.Popen(["uvicorn", "api:app", "--reload"])

# Attendre que l'API démarre
import time

time.sleep(2)


# Lancer l'interface graphique
def call_api():
    try:
        response = requests.get("http://127.0.0.1:8000/get")
        data = response.json()
        print("API Response", f"Response from API: {data['response']}")
    except requests.RequestException as e:
        print("Error", f"Failed to call API: {e}")


call_api()
