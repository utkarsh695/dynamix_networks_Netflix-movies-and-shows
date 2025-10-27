import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Normalize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Handle missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# Split 'duration' into numeric and unit
def split_duration(val):
    if pd.isna(val) or val == 'Unknown':
        return np.nan, np.nan
    parts = val.split()
    try:
        num = float(parts[0])
    except:
        num = np.nan
    unit = parts[1] if len(parts) > 1 else np.nan
    return num, unit

dur_split = df['duration'].apply(split_duration)
df['duration_value'] = dur_split.apply(lambda x: x[0])
df['duration_unit'] = dur_split.apply(lambda x: x[1])

# Extract year from release_year and date_added
df['year_added'] = df['date_added'].dt.year

# Drop duplicates
df = df.drop_duplicates(subset=['title', 'director', 'release_year'])

# Save cleaned dataset
df.to_csv("cleaned_netflix.csv", index=False)

print("✅ Cleaning complete! Saved as 'cleaned_netflix.csv'")
print("Rows:", df.shape[0], "| Columns:", df.shape[1])
