import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '824f8ac4df0c2c85866c09b7db736169'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID = 11269

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    respons_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert respons_get.json()['data'][0]['name'] == 'Tata'

@pytest.mark.parametrize('key, value', [('name', 'Tata'), ('trainer_id', str(TRAINER_ID)), ('id', '151987')])
def test_parametrize(key, value):
    respons_paramrtrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert respons_paramrtrize.json()["data"][0][key] == value
    