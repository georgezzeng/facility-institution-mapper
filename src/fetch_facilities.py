import os
import pandas as pd
import yaml


def extract_insitution_id(yaml_path):
    """extracats institution id based on the yaml file path"""
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
        return data.get("InstitutionID")

def get_facilities(repo="topology"):
    facilities_dict = {}
    for root, dirs, files in os.walk(repo): # Generate the file names in a directory tree by walking the tree either top-down or bottom-up.
        for file in files:
            if file == "FACILITY.yaml":
                yaml_path = os.path.join(root, file) # construct the file path by joining the root and file name
                institution_id = extract_insitution_id(yaml_path)

                facility_name = os.path.basename(os.path.dirname(yaml_path))
                facilities_dict[institution_id] = facility_name

    print(facilities_dict)

    return facilities_dict






