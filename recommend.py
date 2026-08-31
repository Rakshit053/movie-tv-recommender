import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pd.read_csv("data/raw/tmdb_5000_movies.csv")

print("Missing overviews:", movies['overview'].isna().sum())
movies['overview'] = movies['overview'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(movies['overview'])

print("Matrix shape:", matrix.shape)
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(matrix)
print("Similarity shape:", similarity.shape)
indices = pd.Series(movies.index, index=movies['title'])

def recommend(title):
    idx = indices[title]
    scores = pd.Series(similarity[idx], index=movies['title'])
    return scores.sort_values(ascending=False)[1:11]


print(recommend('The Dark Knight'))
