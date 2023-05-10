# Este programa python buscará un clan segun el nombre que le indiques, de no existir el clan, se devolverá "Clan no encontrado"
import requests
import os
import json

url_base = "https://api.clashroyale.com/v1/"
key = os.environ["api_key"]
clan = input("Introduce el nombre del clan (ejemplo capa de ozuna): ")

payload = {'Authorization': 'Bearer ' + key}
url = url_base + "clans"
parametros = {'name': clan}
r = requests.get(url, headers=payload, params=parametros)

if r.status_code == 200:
    data = r.json()
    clans = data.get("items")
    if clans:
        clan_info = clans[0]
        print("Clan Tag:", clan_info.get("tag"))
        print("Clan Name:", clan_info.get("name"))
        print("Clan Type:", clan_info.get("type"))
        print("Clan Badge ID:", clan_info.get("badgeId"))
        print("Clan Score:", clan_info.get("clanScore"))
        print("Clan Members:", clan_info.get("members"))
        print("Required Trophies:", clan_info.get("requiredTrophies"))
        print("Clan Chest Level:", clan_info.get("clanChestLevel"))
        print("Clan Chest Max Level:", clan_info.get("clanChestMaxLevel"))
        print("Clan War Trophies:", clan_info.get("clanWarTrophies"))
        print("Donations Per Week:", clan_info.get("donationsPerWeek"))
        location = clan_info.get("location")
        if location:
            print("Location:")
            print("  Country Code:", location.get("countryCode"))
            print("  Country ID:", location.get("id"))
            print("  Is Country:", location.get("isCountry"))
            print("  Country Name:", location.get("name"))
    else:
        print("Clan no encontrado.")
else:
    print("Error en la busqueda:", r.status_code)
