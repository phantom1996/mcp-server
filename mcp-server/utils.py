import requests
import os

from auth import get_ocrolus_auth_token


def create_ocrolus_book(book_name: str):
    auth_token = get_ocrolus_auth_token()
    response = requests.post(
        url="https://api.ocrolus.com/v1/book/add",
        headers={
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
        },
        json={"name": book_name},
    )
    return response.json()


def upload_files(book_uuid: str, file_paths: list[str]):
    resp = []
    for file_path in file_paths:
        file_path = os.environ.get("DIR_PATH") + file_path
        auth_token = get_ocrolus_auth_token()
        with open(file_path, "rb") as file:
            response = requests.post(
                url=f"https://api.ocrolus.com/v1/book/upload",
                headers={
                    "Authorization": f"Bearer {auth_token}",
                },
                files={"upload": file},
                data={
                    'book_uuid': book_uuid,
                    'doc_name': 'ExampleDocument',
                },
            )
        resp.append(response.json())
    return resp



def get_book_status_ocrolus(book_uuid: str):
    auth_token = get_ocrolus_auth_token()
    return requests.get(
        url=f"https://api.ocrolus.com/v1/book/status?book_uuid={book_uuid}",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


def get_income_calculations(book_uuid: str):
    auth_token = get_ocrolus_auth_token()
    return requests.get(
        url=f"https://api.ocrolus.com/v2/book/{book_uuid}/income/bank-statement-v2",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


def search_book(book_name: str):
    auth_token = get_ocrolus_auth_token()
    return requests.get(
        url=f"https://api.ocrolus.com/v1/books?search={book_name}",
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


def get_income_summary(book_uuid: str):
    auth_token = get_ocrolus_auth_token()
    url = f"https://api.ocrolus.com/v2/book/{book_uuid}/income/summary?guideline=FANNIE_MAE"
    return requests.get(
        url=url,
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


def get_income_calculations_for_borrowers(book_uuid: str):
    auth_token = get_ocrolus_auth_token()
    url = f"https://api.ocrolus.com/v2/book/{book_uuid}/income-calculations?guideline=FANNIE_MAE"
    return requests.get(
        url=url,
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


def get_book_documents(book_uuid: str):
    auth_token = get_ocrolus_auth_token()
    url = f"https://api.ocrolus.com/v1/book/forms?book_uuid={book_uuid}"
    return requests.get(
        url=url,
        headers={
            "Authorization": f"Bearer {auth_token}",
        },
    ).json()


if __name__ == "__main__":
    print(get_income_calculations("6f35f1a9-d8de-4b5e-83f2-e70c0be41bab"))

