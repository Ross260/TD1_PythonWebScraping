"""
 Scraper une liste de films

Objectif : Récupérer les films populaires d’un site comme : Letterboxd

Consigne :
1. Accédez à la page des films populaires sur Letterboxd
2. Récupérez la liste des 6 premiers films.
3. Pour chaque film, extrayez :
-> Le titre
-> L’année de sortie
-> La note IMDb
4. Affichez les résultats sous forme de tableau.

"""

import requests
from bs4 import BeautifulSoup

url = "https://letterboxd.com/"
response = requests.get(url)  # Envoie une requête GET

# Vérifier si la requête est réussie
if response.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")
    html_content = response.text  # Contenu HTML de la page

    # On crée un objet BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(response.text, "html.parser")

    print()
    print(soup.title.string) # titre de la page
    print()

    h2_element = soup.find_all('h2', class_='headline-2')
    notes = soup.find_all('p', class_='like-link-target')

    i = 0
    for h2 in h2_element[:6]:
        i = i + 1
        print(str(i) + "- " + h2.text)

    """j = 0
    for note in notes:
        j = j + 1
        print(str(j) + "- " + note.text)"""

    # Si l'élément <p> est trouvé, chercher la balise <span> à l'intérieur
    for note in notes:
        likes = note.find('span')
        # print(note.text)
        if likes:
            content = likes.text
            print(content)
        else:
            print("Aucune balise <span> trouvée dans le <p>.")
else:
    print(f"Erreur {response.status_code}")
