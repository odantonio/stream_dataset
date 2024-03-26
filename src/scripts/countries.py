import os
import pandas

def country_name(files):
    # Dicionário de países/nacionalidades -> sigla do país, para encontrar nos nomes dos arquivos
    countries = {"brasil": "br", "france": "fr", "italian": "it"}
    dfs =[]
    for items in files:
        try:
            # PANDAS always will create a dataframe like R, so df_temp is a temporary dataframe
            df_temp = pandas.read_excel(items)

            # Obtém o nome do arquivo sem a extensão e sem path
            base_name = os.path.splitext(os.path.basename(items))[0]

            # Divide o nome do arquivo em partes
            parts = base_name.split('_')

            for part in parts:
                # Verifica cada parte com o dicionário. Ao encontrar a na parte a chave, cria uma coluna no arquivo com o valor associado à chave
                for chave, valor in countries.items():
                    if part.lower() == chave:
                        df_temp["Location"] = valor
                        df_temp["file_name"] = base_name
                        dfs.append(df_temp)
        except Exception as e:
            print(f"Error reading file {items}: {e}")
            
    return dfs