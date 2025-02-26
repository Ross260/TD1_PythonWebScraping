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

Bonus :
-> Ajoutez le lien IMDb de chaque film.
-> Stockez les données dans un fichier JSON.

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

    i = 0
    for h2 in h2_element[:6]:
        i = i + 1
        print(str(i) + "- " + h2.text)

    """# Si l'élément <h2> est trouvé, chercher la balise <a> à l'intérieur
    for h2 in h2_element:
        titles = h2.find('a')
        if titles:
            # Récupérer le contenu de la balise <a>
            a_content = titles.string
            print(a_content)
        else:
            print("Aucune balise <a> trouvée dans le <h2>.")"""

else:
    print(f"Erreur {response.status_code}")
