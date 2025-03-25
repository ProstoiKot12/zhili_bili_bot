import os

import requests
import json
from dotenv import load_dotenv


async def get_token():
    load_dotenv()
    url = f'https://{os.getenv("HOSTNAME")}/v2api/auth/login'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'email': os.getenv("EMAIL"),
        'api_key': os.getenv("API_KEY")
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json().get('token')
    else:
        raise Exception(f"Error {response.status_code}: {response.json()}")


async def create_customer(customer_data):
    load_dotenv()
    token = await get_token()
    url = f'https://{os.getenv("HOSTNAME")}/v2api/{os.getenv("BRANCH_ID")}/customer/create'
    headers = {
        'X-ALFACRM-TOKEN': token,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(customer_data))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.json()}")
