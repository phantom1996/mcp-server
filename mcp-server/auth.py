import requests
import os
from functools import lru_cache


@lru_cache(maxsize=1)
def get_ocrolus_auth_token() -> str:
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    url = "https://auth.ocrolus.com/oauth/token"
    response = requests.post(
        url=url,
        data={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        },
    )
    return response.json()['access_token']
