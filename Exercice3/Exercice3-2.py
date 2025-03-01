"""
    Scraper un site e-commerce (Amazon)

Objectif : Extraire les informations sur les produits d’une catégorie spécifique.

Consigne :
1. Choisissez une catégorie sur Amazon (ex : ordinateurs portables,
téléphones).
2. Récupérez les trois premières pages de résultats.
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
import time
import pandas as pd
import openpyxl

# l'url de la page des catégories
url = 'https://www.amazon.com.be/s?bbn=27862509031&rh=n%3A27862509031%2Cp_36%3A28057314031&content-id=amzn1.sym' \
      '.ce555983-ca46-4eb2-90e7-0662b086667f&pd_rd_r=df917085-8e75-46c0-8d67-de203b8b3b40&pd_rd_w=MCQnS&pd_rd_wg' \
      '=J7kU0&pf_rd_p=ce555983-ca46-4eb2-90e7-0662b086667f&pf_rd_r=PENPMCH55R6W0YGPX7SF '
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.5481.104 Safari/537.36"}

# mon dictionnaire de base
data = {
    "Numero": [],
    "Nom_produit": [],
    "Prix": []
}
current_url = url
i = 0
for j in range(1, 4):

    print(f"Page {j}")
    # Envoyer une requête GET à l'URL
    response = requests.get(current_url, headers=headers)
    time.sleep(1)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        print("Requête réussie ! Information du site " + url + " récuperer avec succès ")

        # Parser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify()) # recupère tous les éléments de la page mais de manière formaté

        # Extraction des Noms des articles et leurs prix
        h2_titles = soup.find_all('h2', class_='a-size-base-plus')
        prices = soup.find_all('span', class_='a-price-whole')
        fractions = soup.find_all('span', class_='a-price-fraction')

        for h2, price, fraction in zip(h2_titles, prices, fractions):
            i = i + 1
            # print(f"{i}- {h2.text}   Prix : {price.text}{fraction.text}")

            # Stockage des resultats dans un fichier excel
            data["Numero"].append(i)
            data["Nom_produit"].append(h2.text)
            data["Prix"].append(price.text + fraction.text)

        # Extraction du lien de la prochaine page
        next_link = soup.find("a", class_="s-pagination-item")
        # print("j'arrive ici")
        if next_link:
            # print("j'arrive ici 2")
            current_url = "https://www.amazon.com.be/" + next_link["href"]
            print(current_url)
            time.sleep(1)
        else:
            break

    else:
        print("La requête a échoué avec le code d'état:", response.status_code)

print(data)  # petite vérification du contenu du mon dictionnaire

# transformation en fichier csv
df = pd.DataFrame(data)
df.to_csv("Produit.csv", index=False, encoding="utf-8")

# transformation en fichier excel
# 1. je crée un nouveau classeur excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# 2. j'écrire les en têtes de colonne
sheet.append(list(data.keys()))

# 3. j'écrire les données
for row in zip(*data.values()):
    sheet.append(row)

# 4. j'enregistre le fichier excel
workbook.save("Produits_excel.xlsx")
