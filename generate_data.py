"""
generate_data.py
Generates a synthetic movie ratings dataset and saves it as movies.csv.
"""

import numpy as np
import pandas as pd

np.random.seed(42)

GENRES = [
    "Action", "Comedy", "Drama", "Horror", "Romance",
    "Sci-Fi", "Thriller", "Animation", "Documentary", "Fantasy"
]

# Genre bias: some genres tend to rate higher than others
GENRE_RATING_BIAS = {
    "Action": 6.2,
    "Comedy": 6.0,
    "Drama": 7.0,
    "Horror": 5.5,
    "Romance": 6.3,
    "Sci-Fi": 6.8,
    "Thriller": 6.9,
    "Animation": 7.2,
    "Documentary": 7.5,
    "Fantasy": 6.6,
}

NUM_MOVIES = 800
YEARS = range(1980, 2024)

def generate_title(idx):
    adjectives = ["Dark", "Lost", "Broken", "Silent", "Golden", "Hidden", "Rising", "Falling"]
    nouns = ["World", "Night", "Dream", "City", "Heart", "Shadow", "Journey", "Fire"]
    return f"The {adjectives[idx % len(adjectives)]} {nouns[(idx * 3) % len(nouns)]} {idx + 1}"

rows = []
for i in range(NUM_MOVIES):
    genre = np.random.choice(GENRES)
    year = int(np.random.choice(list(YEARS)))
    base_rating = GENRE_RATING_BIAS[genre]

    # Slight upward trend in ratings over years (modern movies rated slightly higher)
    year_effect = (year - 1980) * 0.01

    rating = np.clip(np.random.normal(loc=base_rating + year_effect, scale=1.0), 1.0, 10.0)
    votes = int(np.random.exponential(scale=50000))

    rows.append({
        "title": generate_title(i),
        "genre": genre,
        "year": year,
        "rating": round(rating, 1),
        "votes": votes,
    })

df = pd.DataFrame(rows)
df.to_csv("movies.csv", index=False)
print(f"Dataset saved to movies.csv ({len(df)} rows)")
print(df.head())