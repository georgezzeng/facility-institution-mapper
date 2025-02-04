import requests


def get_institutions(api_url="https://topology-institutions.osg-htc.org/api/institution_ids"):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        institutions_dict = {}

        for institution in data:
            institution_id = institution["id"]
            institution_name = institution["name"]
            ror_id_url = institution["ror_id"]

            ror_id = ror_id_url.split("/")[-1] if ror_id_url else None

            institutions_dict[institution_id] = {"name": institution_name, "ror_id": ror_id}

        print(institutions_dict)
        return institutions_dict

    else:
        return "Data not found"



