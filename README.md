# Movie Ratings Exploratory Analysis

An exploratory data analysis (EDA) project examining a movie ratings dataset. This project uses Python, Pandas, and Matplotlib/Seaborn to uncover trends in movie ratings across genres, release years, and more.

## Project Overview

This analysis explores:
- Distribution of movie ratings
- Average ratings by genre
- Number of movies released per year
- Rating trends over time

## Tech Stack

- Python 3.8+
- Pandas
- Matplotlib
- Seaborn

## Project Structure

```
movie-ratings-eda/
├── README.md
├── requirements.txt
├── generate_data.py       # Script to generate sample dataset
└── analysis.py            # Main EDA script with all visualizations
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/movie-ratings-eda.git
cd movie-ratings-eda
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the sample dataset

```bash
python generate_data.py
```

This creates `movies.csv` in the project directory.

### 4. Run the analysis

```bash
python analysis.py
```

Charts will be saved as PNG files in the project directory.

## Sample Visualizations

Running the analysis produces four charts:
- `rating_distribution.png` — Histogram of all movie ratings
- `avg_rating_by_genre.png` — Bar chart of average rating per genre
- `movies_per_year.png` — Line chart of movie releases over time
- `rating_trend_by_year.png` — Average rating trend over time

## Dataset

The dataset is synthetically generated for demonstration purposes and includes:
- Movie title
- Genre
- Release year (1980–2023)
- Rating (1.0–10.0)
- Number of votes

## License

MIT