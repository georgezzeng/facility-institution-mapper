import requests


def get_institutions(api_url="https://topology-institutions.osg-htc.org/api/institution_ids"):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Data not found"
    print(response.json())


