from pytz.lazy import LazyDict


def compare_names_and_check_shared_ids(facilities_df, institutions_data):
    """"""
    # Create a dictionary mapping institution IDs to their names from the API data
    institution_dict = {institution["id"]: institution["name"] for institution in institutions_data}

    # Add a column for institution name using the mapping
    facilities_df['institution_name'] = facilities_df['institution_id'].map(institution_dict)

    #compare the facility name and institution name
    facilities_df["same_name"] = facilities_df.apply( lambda x: x["facility_name"] == x["institution_name"], axis=1)

    # Check if there are any shared institution IDs
    facilities_df["shared_institution"] = facilities_df.duplicated(subset=["institution_id"], keep=False)

    return facilities_df