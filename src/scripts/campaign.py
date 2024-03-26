import os
import pandas


def campaign(files):
    dfs=[]
    for items in files:
        try:
            items["campaign"] = items["utm_link"].str.extract(r"utm_campaign=(.*)")
            dfs.append(items)
        except Exception as e:
            print(f"Error reading file {items}: {e}")
    return dfs