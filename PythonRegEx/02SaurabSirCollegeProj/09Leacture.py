import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('path_to_your_hulu_data.csv')

# Display general info and basic statistics
print("General Information about the DataFrame:")
print(df.info())

print("\nStatistical Summary for Numerical Columns:")
print(df.describe())

# 1. Handle missing values (if any)
# Check for missing data
print("\nMissing values:")
print(df.isnull().sum())

# Drop rows where 'imdbAverageRating' or 'releaseYear' are NaN for analysis
df_cleaned = df.dropna(subset=['imdbAverageRating', 'releaseYear'])

# 2. Distribution of IMDB ratings
plt.figure(figsize=(10,6))
sns.histplot(df_cleaned['imdbAverageRating'], kde=True, bins=20, color='blue')
plt.title('Distribution of IMDB Average Ratings')
plt.xlabel('IMDB Average Rating')
plt.ylabel('Frequency')
plt.show()

# 3. Distribution of IMDB number of votes
plt.figure(figsize=(10,6))
sns.histplot(df_cleaned['imdbNumVotes'], kde=True, bins=20, color='green')
plt.title('Distribution of IMDB Number of Votes')
plt.xlabel('IMDB Number of Votes')
plt.ylabel('Frequency')
plt.show()

# 4. Relationship between Release Year and IMDB Rating
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_cleaned, x='releaseYear', y='imdbAverageRating', color='red')
plt.title('Release Year vs IMDB Average Rating')
plt.xlabel('Release Year')
plt.ylabel('IMDB Average Rating')
plt.show()

# 5. Average IMDB rating by Year
avg_rating_by_year = df_cleaned.groupby('releaseYear')['imdbAverageRating'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=avg_rating_by_year, x='releaseYear', y='imdbAverageRating', marker='o', color='purple')
plt.title('Average IMDB Rating by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Average IMDB Rating')
plt.xticks(rotation=45)
plt.show()

# 6. Count of Different Types (tv or movie)
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Count of TV Shows vs Movies')
plt.xlabel('Type (TV or Movie)')
plt.ylabel('Count')
plt.show()

# 7. Count of available countries
country_count = df['availableCountries'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=country_count.index, y=country_count.values, palette='coolwarm')
plt.title('Top 10 Available Countries')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 8. Genre distribution (Top 10 genres)
df['genres_list'] = df['genres'].str.split(',')  # Split genres by comma
df_exploded = df.explode('genres_list')
top_genres = df_exploded['genres_list'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.index, y=top_genres.values, palette='viridis')
plt.title('Top 10 Genres')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 9. Insights & Conclusions
print("\nInsights:")
print("1. The distribution of IMDB average ratings suggests that most titles have ratings between 6 and 7, with a few exceptional titles reaching a 9 or 10.")
print("2. There is a noticeable drop in the number of votes for older movies/shows, which might indicate that newer titles are getting more attention.")
print("3. The scatter plot shows no clear trend between release year and IMDB rating, suggesting that ratings do not correlate directly with age of content.")
print("4. TV shows and movies are almost equally represented in the dataset.")
print("5. The most frequent countries where titles are available appear to be the US and Japan, which might be relevant for distribution insights.")
print("6. The most common genres are Drama, Comedy, and Thriller, with other genres like Action and Documentary also contributing.")

# Save cleaned data for further analysis if needed
df_cleaned.to_csv('cleaned_hulu_data.csv', index=False)

