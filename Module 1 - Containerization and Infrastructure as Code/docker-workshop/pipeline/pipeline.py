import sys
import pandas as pd

print('arguments:', sys.argv)

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})

if len(sys.argv) > 1:
    month = int(sys.argv[1])
    df['month'] = [month] * len(df)
    print(df.head())

    df.to_parquet(f"output_{month}.parquet")

    print(f'hello pipeline, month={month}')