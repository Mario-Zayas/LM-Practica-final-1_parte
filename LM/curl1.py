import requests
import os
import json

url_base = "https://api.clashroyale.com/v1/"
key = os.environ["api_key"]
tag = input("Introduce el tag del jugador (ejemplo 2L2V9U09): ")

filtrar = input("¿Quieres filtrar el resultado? (s/n): ")

if filtrar == "s":
    parametros = input("Introduce el parametro para filtrar (ej. wins, losses, threeCrownWins): ")
    payload = {'Authorization': 'Bearer ' + key}
    url = url_base + "players/%23" + tag
    r = requests.get(url, headers=payload)

    if r.status_code == 200:
        datos = r.json()
        if parametros == "wins":
            print("Wins:", datos.get("wins"))
        elif parametros == "losses":
            print("Losses:", datos.get("losses"))
        elif parametros == "threeCrownWins":
            print("Three Crown Wins:", datos.get("threeCrownWins"))
        else:
            print("Parametro no valido.")
    else:
        print("Error en la busqueda:", r.status_code)

elif filtrar == "n":
    payload = {'Authorization': 'Bearer ' + key}
    url = url_base + "players/%23" + tag
    r = requests.get(url, headers=payload)

    if r.status_code == 200:
        datos = r.json()
        print("Tag:", datos.get("tag"))
        print("Name:", datos.get("name"))
        print("Exp Level:", datos.get("expLevel"))
        print("Trophies:", datos.get("trophies"))
        print("Best Trophies:", datos.get("bestTrophies"))
        print("Wins:", datos.get("wins"))
        print("Losses:", datos.get("losses"))
        print("Battle Count:", datos.get("battleCount"))
        print("Three Crown Wins:", datos.get("threeCrownWins"))
        print("Challenge Cards Won:", datos.get("challengeCardsWon"))
        print("Challenge Max Wins:", datos.get("challengeMaxWins"))
        print("Tournament Cards Won:", datos.get("tournamentCardsWon"))
        print("Tournament Battle Count:", datos.get("tournamentBattleCount"))
        print("Role:", datos.get("role"))
        print("Donations:", datos.get("donations"))
        print("Donations Received:", datos.get("donationsReceived"))
        print("Total Donations:", datos.get("totalDonations"))
        print("War Day Wins:", datos.get("warDayWins"))
        print("Clan Cards Collected:", datos.get("clanCardsCollected"))
        clan = datos.get("clan")
        print("Clan Tag:", clan.get("tag"))
        print("Clan Name:", clan.get("name"))
        print("Clan Badge ID:", clan.get("badgeId"))
    else:
        print("Error en la busqueda:", r.status_code)
