

def shared_institution(df):
    """checks whether the institution is shared between facilities"""
    df["share_institution"] = df.duplicated(subset=["institution_name"], keep=False)
    return df