import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

WIKI_URL = r"https://doughboys.fandom.com/wiki/Episodes"
EXT_FILENAME = './doughboys_episode_data.csv'

def get_wiki_table( wiki_url=WIKI_URL ):
    return pd.read_html(wiki_url)[0]

def get_ext_table( db_wiki_df ):
    db_ext_df = pd.DataFrame()
    for ep_idx in range(len(db_wiki_df)):
        ep_row = db_wiki_df.iloc[ep_idx]
        restaurant, guest_list_1 = process_episode_title(ep_row['Title'])
        guest_list_2 = process_episode_notes(ep_row['Notes'])
        guest_list = guest_list_2 if len(guest_list_2) > len(guest_list_1) else guest_list_1
        ep_row['Topic'] = restaurant
        for guest_idx, guest_name in enumerate(guest_list):
            ep_row[f'Guest {guest_idx+1}'] = guest_name
        db_ext_df = pd.concat([db_ext_df,ep_row.to_frame()],axis=1)
    return db_ext_df.T

def process_episode_title(title):
    title_parts = title.split(' with ')
    n_parts = len(title_parts)
    restaurant = title_parts[0] if n_parts > 1 else np.nan
    guest_list = title_parts[-1].split(' & ') if n_parts > 1 else []
    return restaurant, guest_list

def process_episode_notes(notes):
    if isinstance(notes,str):
        guest_search_1 = re.search(r'^\(guest: (.+?)\)$',notes)
        guest_search_2 = re.search(r'^with (.+?)$',notes)
        if guest_search_1:
            guest_list = guest_search_1.group(1).split(' & ')
        elif guest_search_2:
            guest_list = guest_search_2.group(1).split(', ')
        else:
            guest_list = []
    else:
        guest_list = []
    return guest_list

def main():
    doughboys_wiki_df = get_wiki_table()
    doughboys_ext_df = get_ext_table(doughboys_wiki_df)
    doughboys_ext_df.to_csv(EXT_FILENAME)

if __name__ == "__main__":
    main()
