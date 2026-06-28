import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

print("\nAfter Cleaning:", df.shape)

# Filter Movies
movies = df[df["type"] == "Movie"]

# Top 10 countries
print("\nTop Countries:")
print(df["country"].value_counts().head(10))

# Movies released after 2020
recent = df[df["release_year"] >= 2020]
print("\nMovies after 2020:", len(recent))

# Movies vs TV Shows
print("\nContent Type Count:")
print(df.groupby("type").size())

# Top Ratings
print("\nTop Ratings:")
print(df["rating"].value_counts().head())

# Summary statistics
print("\nSummary:")
print(df.describe(include="all"))

# Graph: Movies vs TV Shows
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("graph.png")
plt.show()