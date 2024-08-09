import matplotlib.pyplot as plt
import seaborn as sns

# Extract the year from 'track_album_release_date' and create a 'year' column
df['year'] = pd.to_datetime(df['track_album_release_date']).dt.year

# Now filter the data for the year 2017 only
df_2017 = df[df['year'] == 2017]

# Calculate the average values for the specified features grouped by genre
average_values = df_2017.groupby('playlist_genre')[['loudness', 'mode', 'speechiness', 'acousticness', 
                                           'instrumentalness', 'liveness', 'valence', 
                                           'tempo', 'duration_ms']].mean()

# Convert duration from milliseconds to minutes
average_values['duration_min'] = average_values['duration_ms'] / 60000
average_values = average_values.drop(columns=['duration_ms'])

# Save the findings to a new CSV file
output_path = '/mnt/data/average_values_2017_by_genre.csv'
average_values.to_csv(output_path)

# Display the first few rows of the result
average_values.head()

# Investigate the relationship between danceability and energy
plt.figure(figsize=(10, 6))
sns.scatterplot(x='danceability', y='energy', data=df_2017)
plt.title('Relationship between Danceability and Energy')
plt.xlabel('Danceability')
plt.ylabel('Energy')
plt.grid(True)
plt.show()

# Investigate correlations between danceability, energy, and other factors
correlation_matrix = df_2017[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                              'instrumentalness', 'liveness', 'valence', 'tempo']].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
