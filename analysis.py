"""
analysis.py
Exploratory analysis of the movie ratings dataset.
Produces four chart PNG files.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Setup ──────────────────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 120

df = pd.read_csv("movies.csv")

print("=== Dataset Overview ===")
print(df.shape)
print(df.dtypes)
print(df.head())
print("\nBasic Statistics:")
print(df.describe())
print(f"\nMissing values:\n{df.isnull().sum()}")

# ── 1. Rating Distribution ─────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["rating"], bins=30, color="steelblue", edgecolor="white", linewidth=0.6)
ax.set_title("Distribution of Movie Ratings", fontsize=14, fontweight="bold")
ax.set_xlabel("Rating (1–10)")
ax.set_ylabel("Number of Movies")
mean_rating = df["rating"].mean()
ax.axvline(mean_rating, color="firebrick", linestyle="--", linewidth=1.5, label=f"Mean: {mean_rating:.2f}")
ax.legend()
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.close()
print("\nSaved: rating_distribution.png")

# ── 2. Average Rating by Genre ─────────────────────────────────────────────────
genre_stats = (
    df.groupby("genre")["rating"]
    .agg(avg_rating="mean", count="count")
    .sort_values("avg_rating", ascending=False)
    .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    genre_stats["genre"],
    genre_stats["avg_rating"],
    color=sns.color_palette("muted", len(genre_stats)),
    edgecolor="white",
)
ax.set_xlim(0, 10)
ax.set_title("Average Movie Rating by Genre", fontsize=14, fontweight="bold")
ax.set_xlabel("Average Rating")
ax.set_ylabel("Genre")
for bar, val in zip(bars, genre_stats["avg_rating"]):
    ax.text(val + 0.1, bar.get_y() + bar.get_height() / 2,
            f"{val:.2f}", va="center", fontsize=9)
plt.tight_layout()
plt.savefig("avg_rating_by_genre.png")
plt.close()
print("Saved: avg_rating_by_genre.png")

# ── 3. Movies Released per Year ────────────────────────────────────────────────
movies_per_year = df.groupby("year").size().reset_index(name="count")

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(movies_per_year["year"], movies_per_year["count"],
        color="steelblue", linewidth=1.8, marker="o", markersize=3)
ax.fill_between(movies_per_year["year"], movies_per_year["count"],
                alpha=0.15, color="steelblue")
ax.set_title("Number of Movies Released per Year", fontsize=14, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("movies_per_year.png")
plt.close()
print("Saved: movies_per_year.png")

# ── 4. Average Rating Trend Over Time ─────────────────────────────────────────
yearly_rating = df.groupby("year")["rating"].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(yearly_rating["year"], yearly_rating["rating"],
        color="darkorange", linewidth=2, marker="o", markersize=3)

# Rolling average (5-year window)
yearly_rating["rolling_avg"] = yearly_rating["rating"].rolling(window=5, center=True).mean()
ax.plot(yearly_rating["year"], yearly_rating["rolling_avg"],
        color="firebrick", linewidth=2.5, linestyle="--", label="5-Year Rolling Avg")

ax.set_title("Average Movie Rating Trend Over Time", fontsize=14, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Average Rating")
ax.legend()
plt.tight_layout()
plt.savefig("rating_trend_by_year.png")
plt.close()
print("Saved: rating_trend_by_year.png")

print("\nAnalysis complete. All charts saved.")