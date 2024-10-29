import requests


def get_institutions(api_url="https://topology-institutions.osg-htc.org/api/institution_ids"):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        institutions_dict = {institution['id']: institution['name'] for institution in data}
        print(institutions_dict)
        return institutions_dict

    else:
        return "Data not found"



