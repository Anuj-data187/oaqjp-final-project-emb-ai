import pandas as pd

# Read the Netflix data
data = pd.read_csv("netflix_data.csv")

# Show full dataset
print("=== NETFLIX DATA ===")
print(data)

# Total titles
print("\n=== TOTAL TITLES ===")
print(data.shape[0])

# Count by type
print("\n=== MOVIES VS TV SHOWS ===")
print(data["type"].value_counts())

# Titles by country
print("\n=== TITLES BY COUNTRY ===")
print(data["country"].value_counts())

# Titles by release year
print("\n=== TITLES BY RELEASE YEAR ===")
print(data["release_year"].value_counts())

# Top genres
print("\n=== TOP GENRES ===")
print(data["listed_in"].value_counts())
# Most common rating
print("\n=== MOST COMMON RATING ===")
print(data["rating"].value_counts().head(1))

# Indian content only
print("\n=== INDIAN CONTENT ===")
print(data[data["country"] == "India"])

# Latest release
print("\n=== LATEST RELEASED TITLE ===")
print(data.sort_values(by="release_year", ascending=False).head(1))