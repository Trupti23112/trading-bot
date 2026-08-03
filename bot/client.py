from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    print("KEY:", api_key)
    print("SECRET:", api_secret)

    client = Client(api_key, api_secret, testnet=True)

    return client