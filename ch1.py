import polars as pl

df = pl.read_csv("./data/titanic_dataset.csv")

print(df.head())

print(df.schema)
