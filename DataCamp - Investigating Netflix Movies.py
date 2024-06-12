import pandas as pd
import matplotlib.pyplot as plt

file_path = 'netflix_data.csv'
netflix_df = pd.read_csv(file_path)

# filter data to remove TV shows
netflix_subset = netflix_df[-netflix_df['genre'].str.contains('TV', case=False)]

# retain selected columns
columns_to_drop = ['show_id', 'type', 'director', 'cast', 'date_added', 'description']
netflix_movies = netflix_subset.drop(columns=columns_to_drop)

# filter for movies that are under 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# assign colours to four genre groups
genre_colors = {
    "Children": "Yellow",
    "Documentaries": "Green",
    "Stand-Up": "Orange",
    "Other": "Blue"
}
colors = []
for index, row in short_movies.iterrows():
    genre = row['genre']
    # Assign colors based on genre groups
    if 'Children' in genre:
        colors.append(genre_colors['Children'])
    elif 'Documentaries' in genre:
        colors.append(genre_colors['Documentaries'])
    elif 'Stand-Up' in genre:
        colors.append(genre_colors['Stand-Up'])
    else:
        colors.append(genre_colors['Other'])

# initialise matplotlib figure object
fix, ax = plt.subplots()

# create scatter plot for movie duration by release year
ax.scatter(short_movies['release_year'], short_movies['duration'], c=colors, label='Genre')

# Set labels and title
ax.set_xlabel('Release Year')
ax.set_ylabel('Duration (Minutes)')
ax.set_title('Movie Duration by Release Year')

# Add legend
ax.legend()

# Show plot
plt.show()
