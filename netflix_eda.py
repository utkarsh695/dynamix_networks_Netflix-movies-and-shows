import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
import subprocess

# Enable inline plotting in VS Code
plt.ion()

# Create an output folder for saved charts
os.makedirs("outputs", exist_ok=True)

# Load cleaned Netflix dataset
df = pd.read_csv("cleaned_netflix.csv")

# --- Basic Overview ---
print(df.info())
print(df.describe(include='all').T)
print("Total null values per column:\n", df.isnull().sum())

# --- 1. Movies vs TV Shows ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', palette='pastel')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/plot1_movies_vs_tv.png", bbox_inches='tight')
plt.show()

# --- 2. Titles Added by Year ---
plt.figure(figsize=(10, 4))
sns.countplot(data=df, x='year_added', hue='type', palette='muted')
plt.title("Titles Added to Netflix by Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/plot2_titles_by_year.png", bbox_inches='tight')
plt.show()

# --- 3. Top 10 Genres ---
df['listed_in'] = df['listed_in'].fillna('')
genres = df['listed_in'].str.split(',').explode().str.strip()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(y=top_genres.index, x=top_genres.values, palette='coolwarm')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("outputs/plot3_top_genres.png", bbox_inches='tight')
plt.show()

# --- 4. Top 10 Countries ---
countries = df['country'].str.split(',').explode().str.strip()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(y=top_countries.index, x=top_countries.values, palette='Blues_d')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Count")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("outputs/plot4_top_countries.png", bbox_inches='tight')
plt.show()

# --- 5. Movie Duration Distribution ---
if 'duration_value' in df.columns:
    movies = df[df['type'] == 'Movie']
    plt.figure(figsize=(8, 5))
    sns.histplot(movies['duration_value'], bins=30, kde=True, color='purple')
    plt.title("Distribution of Movie Durations")
    plt.xlabel("Duration (minutes)")
    plt.tight_layout()
    plt.savefig("outputs/plot5_duration_distribution.png", bbox_inches='tight')
    plt.show()

# --- 6. Interactive Plotly Chart (saved, not opened) ---
fig = px.histogram(df, x='year_added', color='type', nbins=20,
                   title="Netflix Titles Added Over Time (Interactive)")
fig.write_html("outputs/plot6_interactive_titles.html")
print("📊 Interactive chart saved as: outputs/plot6_interactive_titles.html")

# --- Automatically Open Outputs Folder ---
output_path = os.path.abspath("outputs")
system_name = platform.system()

print("\n✅ All charts saved successfully in:", output_path)

try:
    if system_name == "Windows":
        os.startfile(output_path)
    elif system_name == "Darwin":  # macOS
        subprocess.Popen(["open", output_path])
    else:  # Linux
        subprocess.Popen(["xdg-open", output_path])
    print("📂 Opened 'outputs' folder for you!")
except Exception as e:
    print(f"⚠️ Could not open folder automatically: {e}")
