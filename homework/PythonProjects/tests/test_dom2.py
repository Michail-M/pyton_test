import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '824f8ac4df0c2c85866c09b7db736169'
HEADER = {'Content-Type' : 'application/json','trainer_token':TOKEN}
TRAINER_ID = 11269
TRAINER_NAME = 'Misha150'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID, 'trainer_name' : TRAINER_NAME})
    assert response.status_code == 200
    data = response.json()
    assert 'data' in data, "'data' key not found in response"
    assert len(data['data']) > 0, "'data' is empty"
    trainer_name = [trainer['trainer_name'] for trainer in data['data']]
    assert TRAINER_NAME in trainer_name, f"Trainer name '{TRAINER_NAME}' not found in response"

def test_part_of_response():
    respons_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID, 'trainer_name' : TRAINER_NAME})
    assert respons_name.json()['data'][0]['trainer_name'] == 'Misha150'
    
@pytest.mark.parametrize('key, value', [('trainer_name', 'Misha150'), ('id', str(TRAINER_ID))])
def test_parametrize(key, value):
    respons_paramrtrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert respons_paramrtrize.json()["data"][0][key] == value
   