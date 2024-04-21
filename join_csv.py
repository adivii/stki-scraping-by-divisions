import pandas as pd
import os
from tqdm import tqdm

cats = os.listdir('output_csv/')
df = pd.DataFrame()

for i in tqdm(range(len(cats))):
    years = os.listdir(f'output_csv/{cats[i]}/')

    for year in years:
        # print(year)
        temp = pd.read_csv(f'output_csv\\{cats[i]}\\{year}')
        # print(df.head(5))
        df = df._append(temp, ignore_index=True)

# print(cat)
# df = pd.read_csv('combined_data.csv')
# print(df.head(5).T)
df.drop(['Unnamed: 0'], axis=1, inplace=True)
df.to_csv('combined_data.csv', index=False)