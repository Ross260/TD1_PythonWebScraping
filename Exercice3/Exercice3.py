"""
    Scraper un site e-commerce (Cdiscount)

Objectif : Extraire les informations sur les produits d’une catégorie spécifique.

Consigne :
1. Choisissez une catégorie sur Amazon ou Cdiscount (ex : ordinateurs portables,
téléphones).
2. Récupérez la première page de résultats.
3. Extrayez pour chaque produit
-> Le nom du produit
-> Le prix
4. Affichez les ... premiers produits des trois premières pages.

Bonus :
-> Ajoutez un User-Agent pour éviter d’être bloqué.
-> Stockez les résultats dans un fichier Excel

"""

import requests
from bs4 import BeautifulSoup

# l'url de la page des catégories
url = 'https://www.cdiscount.com/b-429955-notre-selection-image-et-son.html#_his_'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.5481.104 Safari/537.36"}

# Envoyer une requête GET à l'URL
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Requête réussie ! Information du site " + url + " récuperer avec succès ")
    html_content = response.text  # Contenu HTML de la page

    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify()) # ne recupère pas tous les éléments de la page

    # Trouver les éléments correspondants à la catégorie
    h2_titles = soup.find_all('h2', class_='prdtTit')

    i = 0
    # Je parcours tous les titres recupérés, les balises <a> trouvées et j'extrais les href
    # j'utilise le zip() ici pour combiner les listes et les parcourir
    for h2 in h2_titles:
        i = i + 1
        print(f"{i}- {h2.string}")
else:
    print("La requête a échoué avec le code d'état:", response.status_code)
