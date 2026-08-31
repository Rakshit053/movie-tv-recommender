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

print("\nTop 10 by rating:")
best = movies.sort_values('vote_average', ascending=False)
print(best[['title', 'vote_average', 'vote_count']].head(10))

mask = movies['vote_count'] >= 1000
print(mask.head())
print(mask.sum())

print("\nTop 10 that people have actually seen:")
popular = movies[mask]
best_popular = popular.sort_values('vote_average', ascending=False)
print(best_popular[['title', 'vote_average', 'vote_count']].head(10)) 
C = movies['vote_average'].mean()
m = movies['vote_count'].quantile(0.90)

qualified = movies[movies['vote_count'] >= m].copy()

v = qualified['vote_count']
R = qualified['vote_average']
qualified['score'] = (v / (v + m)) * R + (m / (v + m)) * C

top = qualified.sort_values('score', ascending=False)
print("\nTop 10 by weighted rating:")
print(top[['title', 'vote_average', 'vote_count', 'score']].head(10))