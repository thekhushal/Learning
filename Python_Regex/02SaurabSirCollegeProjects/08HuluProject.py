import pandas as pd

# Load the CSV file
file_path = 'newdata.csv'  # Replace with your CSV file's path
df = pd.read_csv("/home/theta/CODE/Learning/Python_Regex/newdata.csv")


print("General info about the DataFrame: ", df.info())  # General info about the DataFrame
print("Statistical summary for numerical columns: ", df.describe())  # Statistical summary for numerical column
print("Shape of data: (rows, columns) ", df.shape)  # Get number of rows and columns (rows, columns)
for i in range(len(df.columns)):
    print(f"List of column names ({i+1}): ", df.columns[i])  # List of column names
print(df.tail())  # Select the first 5 rows

# # Top 10 highest-rated content
# top_rated = df.sort_values(by='imdbAverageRating', ascending=False).head(10)
# print("Top 10 Highest-Rated Content:\n", top_rated[['title', 'imdbAverageRating', 'genres']])

# print("______________________________________1_________________________________________")

# # Explode genres into individual rows for analysis
# df['genres'] = df['genres'].fillna("Unknown")  # Replace NaN with "Unknown"
# genres_df = df.assign(genres=df['genres'].str.split(', ')).explode('genres')
# # 
# # Average rating per genre
# avg_rating_per_genre = genres_df.groupby('genres')['imdbAverageRating'].mean().sort_values(ascending=False)
# print("Average Rating Per Genre:\n", avg_rating_per_genre)


# print("_______________________________________2________________________________________")

# # Average rating by release year
# rating_by_year = df.groupby('releaseYear')['imdbAverageRating'].mean()
# rating_by_year.plot(kind='line', title='Average Rating by Release Year')

# print("________________________________________3_______________________________________")

# # Count of content per country
# country_content_count = df['availableCountries'].value_counts()
# print("Content Available Per Country:\n", country_content_count.head(10))

# print("_______________________________________4________________________________________")

# # Average rating and votes for movies vs. shows
# type_analysis = df.groupby('type')[['imdbAverageRating', 'imdbNumVotes']].mean()
# print("Movies vs. Shows Analysis:\n", type_analysis)

# print("________________________________________5_______________________________________")

# # Save insights to CSV
# top_rated.to_csv('top_rated_content.csv', index=False)
# avg_rating_per_genre.to_csv('avg_rating_per_genre.csv')

# print("_________________________________________6_____________________________________")