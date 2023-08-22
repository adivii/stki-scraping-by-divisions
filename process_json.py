import json
import pandas as pd
import os
from tqdm import tqdm

output_path = 'output_csv/'
cats = os.listdir('output')

for i in tqdm(range(len(cats))):
    if not os.path.exists(output_path + cats[i]  + '/'):
        os.makedirs(output_path + cats[i]  + '/')

    years = os.listdir(f'output/{cats[i]}/')

    for year in years:
        # print(year)
        df = pd.read_json(f'output\\{cats[i]}\\{year}')
        # print(df.head(5))
        df.to_csv(output_path + cats[i] + f'/{year[:-5]}.csv')

# print(cat)
# df = pd.read_json('output\\FMIPA1\\2000.json')
# print(df.head(5))