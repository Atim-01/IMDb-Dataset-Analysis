#!/usr/bin/env python
# coding: utf-8

# ## Analyzing the Cleaned Data

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


file_path = "C:\\Users\\Administrator\\DS Project Portfolio\\cleaned_IMDb_dataset.csv"
data = pd.read_csv(file_path, encoding='latin1')
data.sample(5)


# 1. **Score vs. Income Correlation analysis** 
# 
# Let's examines the relationship between a movie's audience rating (Score) and its financial performance (income). The goal is to determine whether higher-rated movies tend to earn more revenue or if there's a disconnect between critical acclaim and box office success. This analysis helps in understanding the extent to which audience satisfaction influences a movie's profitability.

# #### Exploratory Data Analysis (EDA) for the Score vs. Income Correlation.

# - Summary Statistics for 'Score' and 'Income ($)'

# In[7]:


summary_stats = data[['Score', 'Income ($)']].describe()
print(summary_stats)


# - Visualizing Distributions

# In[8]:


# Histogram for Score
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(data['Score'], bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')

# Histogram for Income ($)
plt.subplot(1, 2, 2)
plt.hist(data['Income ($)'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Income ($)')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


# - Scatter plot for Score vs. Income ($)

# In[9]:


plt.figure(figsize=(8, 6))
plt.scatter(data['Score'], data['Income ($)'], color='purple', alpha=0.5)
plt.title('Score vs. Income ($)')
plt.xlabel('Score')
plt.ylabel('Income ($)')
plt.show()


# - There no correlation between the Score of the movies and the Income gotten from it. 
# 
# **Possible Explanations:**
# 1. **Niche Audience:** Some movies with high scores might cater to a niche audience, leading to lower income despite good ratings.
# 2. **Marketing and Distribution:** Movies with lower scores might still generate significant income due to strong marketing, wide distribution, or being part of a popular franchise.
# 3. **Budget Constraints:** Low-budget films, which often have lower income, might still receive good scores if they are critically acclaimed.

# ### Further Analysis for this
# Let's explore other factors that might influence income, such as Genre, Country, or Content Rating, to see if there’s a more complex interaction affecting income.

# 1. Income by Genre Analysis
# - **Objective:** Determine which genres are associated with higher or lower income.

# In[10]:


# Grouping by Genre and calculating the average income
genre_income = data.groupby('Genre')['Income ($)'].mean().sort_values(ascending=False)

# Plotting the average income by Genre
plt.figure(figsize=(10, 8))
sns.barplot(x=genre_income.values, y=genre_income.index, palette='viridis')
plt.title('Average Income by Genre')
plt.xlabel('Average Income ($)')
plt.ylabel('Genre')
plt.show()


# **Interpretation:**
# - **Top-Earning Genres:** Action, Adventure, Drama
# - **Low-Earning Genres:** Adventure, Mystery, Thriller

# 2. Income by Country
# - **Objective:** Identify if certain countries produce movies with higher incomes.
# 

# In[11]:


# Group by 'Country' and calculate the average income
country_income_avg = data.groupby('Country')['Income ($)'].mean().sort_values(ascending=False)

# Plotting the average income by Country
plt.figure(figsize=(12, 8))
sns.barplot(x=country_income_avg.values, y=country_income_avg.index, palette='viridis')
plt.title('Average Movie Income by Country')
plt.xlabel('Average Income ($)')
plt.ylabel('Country')
plt.show()


# **Interpretation:**
# - **Top Countries:** New Zealand, USA and France (in descending order) are the leading countries with highest returns
# 
# (The countries at the top of the chart have the highest average incomes, indicating that movies from these countries tend to perform well financially.)
# - **Bottom Countries:** Denmark, Iran and Brazil (in ascending order) are the countries with least returns
# 
# (The countries at the bottom have lower average incomes, suggesting that movies from these regions might not generate as much revenue on average.)

# 3. Income by Content Rating
# 
# **Objective:** Examine if the Content Rating of a movie (e.g., PG, R) influences its income.
# 

# In[12]:


# Grouping by 'Content Rating' and calculating the average income
content_rating_income_avg = data.groupby('Content Rating')['Income ($)'].mean().sort_values(ascending=False)

# Plotting the average income by Content Rating
plt.figure(figsize=(10, 6))
sns.barplot(x=content_rating_income_avg.values, y=content_rating_income_avg.index, palette='coolwarm')
plt.title('Average Movie Income by Content Rating')
plt.xlabel('Average Income ($)')
plt.ylabel('Content Rating')
plt.show()


# **Interpretation:**
# - **Higher Average Income Ratings:** Movies rated PG-13 evidently appeals to a wider demographic, leading to higher average incomes.
# - **Lower Average Income Ratings:** Movies rated R evidently have the least appeal.

# 4. Top-Performing Movie Genres by Revenue Across Countries
# 
# **Objective:** To identify the movie genres that generate the highest revenue in each country.

# In[15]:


# Ensure no scientific notation is used for displaying numbers
pd.options.display.float_format = '{:,.2f}'.format

# Group by 'Country' and 'Genre', then sum the 'Income ($)'
grouped_data = data.groupby(['Country', 'Genre'])['Income ($)'].sum().reset_index()

# Find the genre with the highest income in each country
best_genre_per_country = grouped_data.loc[grouped_data.groupby('Country')['Income ($)'].idxmax()]

# Sort the result by 'Income ($)' in descending order
best_genre_per_country = best_genre_per_country.sort_values(by='Income ($)', ascending=False).reset_index(drop=True)
best_genre_per_country


# ### Conclusion:
# The analysis highlights that certain genres, countries, and content ratings are associated with higher movie incomes. 
# 
# Action, Adventure, and Drama genres, as well as movies from New Zealand, USA, and France, generally perform better financially. 
# 
# Additionally, PG-13 rated movies have the widest appeal, leading to higher revenues. 
# 
# Furthermore, we see the the genre that generate the highest revenue in each country in the dataset.
# 
# These insights can inform decisions in film production, marketing strategies, and distribution to maximize financial success.

# In[ ]:




