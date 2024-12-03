import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '824f8ac4df0c2c85866c09b7db736169'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}

body_regestration = {
    "trainer_token": TOKEN,
    "email": "Misha150@mail.ru",
    "password": "Iloveqa1"
}
boby_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_rename = {
    "pokemon_id": "id",
    "name": "New Name",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "id"
}

'''respons = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_regestration)
print(respons.text)'''

'''respons_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json = boby_confirmation)
 print(respons_confirmation.text)'''

respons_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(respons_create.text)

massage = respons_create.json()
print(massage)

respons_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(respons_rename.text)
massage = respons_rename.json()
print(massage)

respons_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(respons_add_pokeball.text)
massage = respons_add_pokeball.json()
print(massage)