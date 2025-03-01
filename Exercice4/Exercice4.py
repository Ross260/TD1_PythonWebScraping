"""
 Scraper des données météorologiques

Objectif : Obtenir et afficher la météo d’une ville en temps réel.

Consigne :
1. Trouvez un site météo qui affiche les températures par ville La chine Météo.
2. Récupérez la température actuelle pour une ville donnée.
3. Affichez-la sous forme d’un message : "La température à Paris est de 15°C."

"""

import requests
from bs4 import BeautifulSoup

url = "https://www.lachainemeteo.com/meteo-france/ville-33/previsions-meteo-paris-aujourdhui"
reponse = requests.get(url)

if reponse.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")

    soup = BeautifulSoup(reponse.text, "html.parser")

    # print(soup.prettify())
    print("\n" + soup.title.string + "\n")

    temperature = soup.find('div', class_='quarter-temperature')
    if temperature.text:
        actual_temp = soup.find('span', class_='tempe')
        ressenti = soup.find('span', class_='tempeFelt')

        print(f"La température actuelle à Paris est de {actual_temp.string}C")
        print(ressenti.string)

else:
    print(f"Erreur {reponse.status_code}")