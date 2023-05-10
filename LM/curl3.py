import requests
import os
import json

url_base = "https://api.clashroyale.com/v1/"
key = os.environ["api_key"]

payload = {'Authorization': 'Bearer ' + key}
url = url_base + "globaltournaments"

r = requests.get(url, headers=payload)
if r.status_code == 200:
    data = r.json()
    globaltournaments = data.get("items")
    if globaltournaments:
        print("Torneos globales:")
        for tournament in globaltournaments:
            print(json.dumps(tournament, indent=2))
    else:
        print("No hay torneos globales disponibles.")
else:
    print("Error en la búsqueda:", r.status_code)
