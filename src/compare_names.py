


def compare_names(df):
    df["same_facility_institution_name"] = df.apply(lambda x: x["facility_name"] == x["institution_name"], axis=1)

    df["same_facility_ror_name"] = df.apply(lambda x: x["facility_name"] == x["ror_name"], axis=1)
    return df
