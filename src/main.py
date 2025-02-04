import pd

from fetch_facilities import get_facilities
from fetch_institutions import get_institutions
from src.combined_df import combine_facilities_and_institutions
from src.compare_names import compare_names
from src.share_institution import shared_institution


def main():
    # get_institutions()
    #
    # get_facilities()

    institutions_dict = get_institutions()
    facilities_dict = get_facilities()
    df = combine_facilities_and_institutions(facilities_dict, institutions_dict)

    df = compare_names(df)
    # count = df["same_name"].value_counts()
    # print(count)
    shared_institution(df).to_excel("data/facility_institution_matcher.xlsx", index=False)
    # facilities_df = get_facilities()
    #
    # facilities_df = compare_names_and_check_shared_ids(facilities_df, institutions)
    #
    # output_csv_file = "data/output.csv"
    #
    # save_to_csv(facilities_df, output_csv_file)
    #
    # print("Data saved to output.csv")

if __name__ == '__main__':
    main()


