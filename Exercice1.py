"""
Scraper les actualités d’un site d’information

Objectif : Récupérer les titres des articles d’un site d’actualités et les afficher proprement.

1. Choisissir un site d’actualités : Le Monde
2. Récupérez la page d’accueil avec : utilisation de la bibliothèque (requests).
3. Utilisez BeautifulSoup pour extraire les titres des articles.
4. Affichez-les proprement sous forme de liste.

Bonus:
-> Ajoutez le lien de chaque article à côté du titre.
-> Stockez les résultats dans un fichier CSV.
"""

import requests
from bs4 import BeautifulSoup
import csv

url = "https://lemonde.fr/"  # Site de livres à scraper
response = requests.get(url)  # Envoie une requête GET

# Vérifier si la requête est réussie
if response.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")
    html_content = response.text  # Contenu HTML de la page

    # On crée un objet BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Affichage du html de manière plus lisible
    print(soup.title.string)

    # recherche de tous les paragraphes <p> sur la page web avec pour classe "article__title"
    # car d'après mon analyse c'est eux qui contiennent les titres des articles
    titles = soup.find_all('p', class_='article__title')

    # QUESTION BONUS
    # Trouver toutes les balises <a> avec la classe "article article--list" d'après mon analyse sur le site
    links = soup.find_all('a', class_='article')

    i = 0
    # Je parcours tous les titres recupérés, les balises <a> trouvées et j'extrais les href
    # j'utilise le zip() ici pour combiner les listes et les parcourir
    for title, link in zip(titles[:20], links[:20]):
        i = i + 1
        href = link.get('href')
        print(f"{i}- {title.string}  {href}")

    # Création du fichier CSV en mode écriture
    with open("Scraping.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Écrire l'en-tête
        writer.writerow(["Numéro", "Titre", "Lien"])

        # Insérer les données extraites
        for i, (title, link) in enumerate(zip(titles[:20], links[:20]), start=1):
            href = link.get('href')
            writer.writerow([i, title.string, href])

    print("Les résultats ont été enregistrés dans le fichier csv avec succès")
else:
    print(f"Erreur {response.status_code}")