import pandas as pd
from pytz.lazy import LazyDict


def combine_facilities_and_institutions(facilities_dict, institutions_dict):
    combined_list = []

    for facility in facilities_dict:
        institution_id = facility["institution_id"]
        facility_name = facility["facility_name"]
        institution_name = institutions_dict.get(institution_id)
        combined_list.append({"institution_id": institution_id, "facility_name": facility_name, "institution_name": institution_name})

    df = pd.DataFrame(combined_list)
    return df

