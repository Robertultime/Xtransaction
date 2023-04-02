import requests
import json

# Configuration de l'API de Pinata
url = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
headers = {
    'pinata_api_key': 'votre_api_key',
    'pinata_secret_api_key': 'votre_secret_api_key',
}

# Données à ajouter sur Pinata
data = {
  "name": "Sac Plume fourre-tout 45 chimères Pégase",
  "description": "L'animation Chimères : Un bestiaire inattendu pour une animation exceptionnelle ! Des créatures de rêves issues de récits mythologiques et de céramiques antiques grecques s’emparent du Bolide 1923-45, du Plume fourre-tout 45 et du Cityback 27. Grâce à la technique du tuffetage, broderie réalisée à même le cuir, puis rasée en surface, les monstres prennent un effet velours. Ces chimères épousent la forme de l’objet et prennent vie à travers la douceur de leur pelage.",
  "brand": "LVMH",
  "thumbnailUri": "ipfs://QmU6d6YpiKbuJowCCwCiWZM8e1S1ZSewfiqBYzgEWUzje9",
  "serieSize": "1000",
  "home":"https://www.hermes.com/fr/fr/product/sac-plume-fourre-tout-45-chimeres-pegase-H078518CKAB/",
  "inceptionPriceEUR":"27000",
  "inceptionDate":"02-04-2023"
}

json_data = json.dumps(data)

# Envoi des données sur Pinata
response = requests.post(url, headers=headers, data=json_data)

# Vérification de la réponse
if response.status_code == 200:
    print("Les données ont été ajoutées sur Pinata avec succès !")
else:
    print("Erreur lors de l'ajout des données sur Pinata :", response.text)