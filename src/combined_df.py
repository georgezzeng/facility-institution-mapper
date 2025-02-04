import pandas as pd
from pytz.lazy import LazyDict
from fetch_ror_name import fetch_ror_name

def combine_facilities_and_institutions(facilities_dict, institutions_dict):
    combined_list = []

    for facility in facilities_dict:

        institution_id = facility["institution_id"]
        facility_name = facility["facility_name"]

        institution_data = institutions_dict.get(institution_id)
        if not institution_data:
            institution_name, ror_id, ror_name = None, None, None
        else:
            institution_name = institution_data.get("name")
            ror_id = institution_data.get("ror_id")
            ror_name = fetch_ror_name(ror_id)



        combined_list.append({"institution_id": institution_id, "facility_name": facility_name, "institution_name": institution_name, "ror_id": ror_id, "ror_name": ror_name})

    df = pd.DataFrame(combined_list)
    return df

