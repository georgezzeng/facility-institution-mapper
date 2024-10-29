


def compare_names(df):
    df["same_name"] = df.apply(lambda x: x["facility_name"] == x["institution_name"], axis=1)
    return df
