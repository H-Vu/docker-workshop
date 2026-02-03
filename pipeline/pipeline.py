import sys
import pandas as pd

print("argument: ", sys.argv)

month = sys.argv[1]

df = pd.DataFrame({"days": [1, 2], "number_passangers": [3, 4]})
print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f"argument 2: month={month}")

