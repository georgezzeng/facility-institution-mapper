**Project Overview**
This project aims to compare facility names (derived from directory names) against institution names fetched from an API. The purpose is to determine whether these names are identical and to check if there are multiple facilities sharing the same institution name. The results are exported into a CSV file with specific columns.

**CSV Structure**
sacility_name: This column holds the name of the facility.
snstitution_name: The official name of the institution.
same_name: A boolean value indicating whether the facility name matches the institution name exactly.
share_institution: A boolean value indicating whether there are other rows in the CSV that share the same institution name.
