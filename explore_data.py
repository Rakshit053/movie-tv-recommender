import pandas as pd

movies = pd.read_csv("data/raw/tmdb_5000_movies.csv")

print("Shape:")
print(movies.shape)

print("\nColumns:")
print(movies.columns)

print("\nFirst 3 rows:")
print(movies.head(3))

print("\nLast 5 rows:")
print(movies.tail())

print("\nData types:")
print(movies.dtypes)