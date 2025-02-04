import requests

def fetch_ror_name(ror_id):
    if not ror_id:
        return None

    ror_url = f"https://api.ror.org/organizations/{ror_id}"
    response = requests.get(ror_url)

    if response.status_code == 200:
        data = response.json()
        return data.get("name")
    else:
        return None
