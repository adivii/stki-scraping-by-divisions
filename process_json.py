import json
import pandas as pd

df = pd.read_json('output\\FMIPA1\\2000.json')
print(df.head(5))