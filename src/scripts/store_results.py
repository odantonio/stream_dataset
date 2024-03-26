import os
import pandas


def store_results(dfs):
    path = "data//ready"
    if not dfs:
        print("No files to store. Exiting.")
    else:
        # concatena todas as tabelas no dfs em uma única tabela
        result = pandas.concat(dfs, ignore_index=True)
        output = os.path.join(path,"transformed.xlsx")
        writer = pandas.ExcelWriter(output,engine="xlsxwriter")
        result.to_excel(writer, index=False)
        writer.close()
# end def 