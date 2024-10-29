

def shared_institution(df):
    """checks whether the institution is shared between facilities"""
    df["share_institution"] = False

    # Group by institution_name and count occurrences
    counts = df.groupby('institution_name')['facility_name'].transform('count')

    # Results in True if count > 1 and institution_name is not null
    df["share_institution"] = (counts > 1) & df['institution_name'].notna()

    return df