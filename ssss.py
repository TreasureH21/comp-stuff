import pandas as pd

movies_data = {
    "Name": ["Dangal", "Interception", "Dead Poets Society", 
             "Interstellar", "Dilwale Dulhaniya le Jaenge", 
             "Tennet", "500 Days of Summer", "Fight Club", 
             "I Want to eat your Pancreas", "Your Lie in April"],
    
    "Language": ["Hindi", "English", "English", "English", 
                 "Hindi", "English", "English", "English", 
                 "Japanese", "Japanese"],
    
    "Genre": ["Sports", "Thriller", "Drama", "Sci-Fi", 
              "Romance", "Sci-Fi", "Romance", "Action", 
              "Romance", "Romance"],
    
    "Rating": [9.0, 9.5, 9.8, 9.9, 9.5, 9.7, 9.8, 8.9, 10.0, 9.5],
    
    "Review": ["Excellent", "Amazing", "Extra Ordinary", 
               "Just marvellous", "Romantic Masterpiece", 
               "Visually Stunning", "Exquisitely Beautiful", 
               "Action Packed", "Peak of Romance Anime", 
               "Can make you cry"]
}
# Create dataframe
df_movie = pd.DataFrame(movies_data)

# Save to CSV
df_movie.to_csv("Movies.csv", index=False)

# Read CSV
df = pd.read_csv("Movies.csv")

# Highest rated movie
highest_rated = df.loc[df["Rating"].idxmax(), "Name"]
print("The highest rated movie is:", highest_rated)

# Filter Hindi movies
hindi_movies = df[df["Language"] == "Hindi"]

# Save Hindi movies
hindi_movies.to_csv("HindiMovies.csv", index=False)

print("Separate CSV file for Hindi Movies created successfully.")

# Read and display Hindi movies
df_hindi = pd.read_csv("HindiMovies.csv")
print(df_hindi)
