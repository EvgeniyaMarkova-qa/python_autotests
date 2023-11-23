import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                         json={
                             "name": "generate",
                             "photo": "generate"
                              },
                              headers={"trainer_token": "c75d5903558e5cc77020ba3a91c79c87",'Content-Type': 'application/json'}, timeout=5)


print(f'Code: {response.status_code}. Message: {response.text}')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                         json={
                             "pokemon_id": "20395",
                             "name": "top",
                             "photo": "https://dolnikov.ru/pokemons/albums/877.png"
                              },
                              headers={"trainer_token": "c75d5903558e5cc77020ba3a91c79c87",'Content-Type': 'application/json'}, timeout=5)


print(f'Code: {response.status_code}. Message: {response.text}')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                         json={
                              "pokemon_id": "20395"
                              },
                              headers={"trainer_token": "c75d5903558e5cc77020ba3a91c79c87",'Content-Type': 'application/json'}, timeout=5)


print(f'Code: {response.status_code}. Message: {response.text}')