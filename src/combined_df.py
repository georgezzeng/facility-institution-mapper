import pandas as pd
from pytz.lazy import LazyDict


def combine_facilities_and_institutions(facilities_dict, institutions_dict):
    combined_list = []

    for institution_id, facility_name in facilities_dict.items():
        institution_name = institutions_dict.get(institution_id)
        combined_list.append({"facility_name": facility_name, "institution_name": institution_name})

    df = pd.DataFrame(combined_list)
    return df

