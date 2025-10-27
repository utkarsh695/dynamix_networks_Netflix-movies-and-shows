# 🎬 Netflix Movies & TV Shows Analysis Dashboard

## 📖 Overview
This project analyzes **Netflix’s catalog** of movies and TV shows to uncover insights about content trends, genres, ratings, release years, and country-wise distribution.  
The analysis involves **data cleaning**, **exploratory data analysis (EDA)** using Python, and **interactive visualizations** using **Power BI**.

---

## 🧾 Dataset
**Source:** [Netflix Movies and TV Shows - Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

The dataset contains information such as:
- `show_id`: Unique identifier for each title  
- `type`: Movie or TV Show  
- `title`: Title of the content  
- `director`, `cast`, `country`: Metadata  
- `date_added`: When it was added to Netflix  
- `release_year`: Year of release  
- `rating`: Age rating  
- `duration`: Duration of the movie or number of seasons  
- `listed_in`: Genre(s)  
- `description`: Summary  

---

## 🧹 Data Cleaning (Python)

Data cleaning was performed using **Pandas** and **NumPy**.  
The following steps were included:
- Removed duplicates and null values  
- Standardized date formats  
- Extracted `year_added` from `date_added`  
- Split `duration` into:
  - `duration_value` (numeric)
  - `duration_type` (“min” or “seasons”)
- Normalized text fields (genres, countries)

Cleaned dataset saved as:  
```bash
cleaned_netflix.csv



📊 Exploratory Data Analysis (EDA)

EDA was performed using:

Pandas for data manipulation

Matplotlib & Seaborn for static plots

Plotly for interactive visualization

Key Insights:

📈 Movies dominate Netflix’s catalog, but TV shows have been growing steadily.

🌎 United States, India, and the UK are the top contributors of Netflix content.

🎭 International Movies and Dramas are the most common genres.

⏱️ Average movie duration ranges between 90–110 minutes.

🗓️ Netflix’s content library expanded significantly after 2015.

🧠 Tools & Technologies
Category	Tools Used
Data Cleaning & EDA	Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly
Visualization	Power BI
Dataset Source	Kaggle
Version Control	Git, GitHub
📈 Power BI Dashboard

An interactive Power BI dashboard was created from the cleaned dataset.

Dashboard Features:

📊 Movies vs TV Shows comparison

📅 Titles added by year

🎬 Top 10 genres

🌍 Top countries producing Netflix content

🎥 Ratings distribution (Pie chart)

🗺️ Map showing country-wise content

⏱️ Movie duration distribution

🎚️ Interactive slicers (by type, year, rating, country)


Snapshot-
!Alt()
