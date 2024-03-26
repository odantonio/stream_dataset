import os
import glob

from scripts.countries import country_name
from scripts.campaign import campaign
from scripts.store_results import store_results

def main():
    dir_path = "data//raw"
    sheet_list = glob.glob(os.path.join(dir_path, "*.xlsx"))
    if not sheet_list:
        print("No files are found. Exiting.")
    else:
        # busca e acrescenta a coluna país de origem da planilha
        alter_sheet = country_name(sheet_list)
        # acrescenta uma coluna com o nome original da planilha
        results = campaign(alter_sheet)
        # salva os dados em outra planilha
        store_results(results)

if __name__ == "__main__":
    main()
# end main