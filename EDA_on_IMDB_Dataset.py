#!/usr/bin/env python
# coding: utf-8

# ### PURPOSE OF THIS PROJECT
# The purpose of this work is to analyze key factors that influence the financial success of movies. By examining the relationship between movie genres, countries of origin, content ratings, and their corresponding incomes, the study aims to identify patterns and trends that can inform decision-making in film production and distribution. The insights derived from this analysis can help filmmakers, producers, and marketers optimize their strategies to maximize box office returns and target the most profitable segments of the movie industry.

# #### Starting With Data Cleaning 

# In[2]:


import pandas as pd


# In[3]:


file_path = 'C:/Users/Administrator/Downloads/messy_IMDB_dataset.csv'

# Load the Data
try:
    # Read the CSV file
    data = pd.read_csv(file_path, delimiter=';', encoding='latin1', on_bad_lines='skip')
except Exception as e:
    print(f"Error reading the file: {e}")


# In[4]:


data.sample(4)


# In[5]:


data.info()


# In[6]:


# Clean and process the DataFrame as needed
data.columns = data.columns.str.strip()


# In[7]:


data


# ### Dealing with the 'Unnamed: 8' column

# In[8]:


data['Unnamed: 8'].isnull().sum()


# In[9]:


data['Unnamed: 8'].unique()


# In[10]:


# All its values are null, hence this column is not needful. I will drop it
data.drop(columns=['Unnamed: 8'], inplace=True)


# In[11]:


data.sample(3)


# ### Dealing with the 'Income' column

# In[12]:


# I want to change the column content to float data type
data["Income"].unique()


# In[13]:


data['Income'] = data['Income'].str.replace('$', '', regex=True)
data.sample(3)


# In[14]:


data['Income'] = data['Income'].str.replace('o', '0', regex=True)
data.sample(3)


# In[15]:


data['Income'].str.strip()


# In[16]:


data['Income'] = data['Income'].str.replace(',', '', regex=True)
data['Income'].sample(3)


# In[17]:


data['Income'] = data['Income'].astype(float)  # Changing the data type


# In[18]:


data['Income'].info()


# In[19]:


data.sample(4)


# In[20]:


data['Income'].unique()


# In[21]:


pd.set_option('display.float_format', lambda x: '%.2f' % x) # I dont want it to display in scientific form


# ### I want to rename some of the column headers

# In[22]:


data = data.rename(columns={'Original titlÊ': 'Original title', 'Genrë¨': 'Genre', 'Duration':'Duration (mins)', 'Income':'Income ($)'})


# In[23]:


data.sample(3)


# ### Dealing with the 'Release year' column

# In[24]:


invalid_dates = data[data['Release year'].isna()]
invalid_dates


# In[25]:


data['Release year'].sample(3)


# In[26]:


data['Release year'] = pd.to_datetime(data['Release year'], dayfirst=True, errors='coerce')


# In[27]:


data['Release year'].info()


# In[28]:


data['Release year'].head(2)


# ### Dealing with the 'Duration (mins)' column

# In[29]:


data['Duration (mins)'].unique()


# In[30]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('c', '', regex=True)


# In[31]:


data['Duration (mins)'].unique()


# In[32]:


specific_date = 'Not Appliable'  # Example specific date to search for

specific_rows = data[data['Duration (mins)'] == specific_date]
specific_rows


# In[33]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('Not Appliable', 'nan', regex=True)


# In[34]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('-', 'nan', regex=True)


# In[35]:


data['Duration (mins)'].unique()


# In[36]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace(' ', 'nan', regex=True)
data['Duration (mins)'] = data['Duration (mins)'].str.replace('Nan', 'nan', regex=True)


# In[37]:


data['Duration (mins)'].unique()


# In[38]:


data['Duration (mins)'] = data['Duration (mins)'].astype(float)  # Changing the data type


# In[39]:


data['Duration (mins)'].info()


# In[40]:


data.sample(5)


# In[41]:


data.info()


# ### Dealing with 'Votes' column

# In[42]:


data['Votes'].unique()


# In[43]:


data['Votes'] = data['Votes'].str.replace('.', '', regex=True).astype(float)  # Changing the data type


# In[44]:


data['Votes'].sample(5)


# In[45]:


data.info()


# ### Dealing with the 'Country' column

# In[46]:


data['Country'].unique()


# In[47]:


# Dictionary mapping old values to new values
replacements = {
    'US': 'USA',
    'US.': 'USA',
    'New Zesland': 'New Zealand',
    'New Zeland': 'New Zealand',
    'West Germany': 'Germany',
    'Italy1': 'Italy'
}

# Replace values in 'Country' column
data['Country'] = data['Country'].replace(replacements)

data['Country'].unique()


# In[48]:


data['Original title'].sample(5)


# ### Others

# In[49]:


data.iloc[13] #Noticed this row with all null values. Let's confirm 


# In[50]:


rows_with_nan = data[data.isna().all(axis=1)] # Let's see if there are other like it
rows_with_nan


# In[51]:


data = data.drop(index=13)


# In[52]:


data.head(15) 


# ### Dealing with the "Content Rating" column

# In[53]:


data['Content Rating'].isnull().sum()


# In[54]:


data['Content Rating'].unique()


# In[55]:


# I want to see how many rows have the 'Approved' has the value for this column
approved_rows = data[data['Content Rating'] == 'Approved']
approved_rows


# In[56]:


# Changing 'Approved' to 'G'
data['Content Rating'] = data['Content Rating'].str.replace('Approved', 'G', regex=True)


# In[57]:


data['Content Rating'].unique()


# In[58]:


unrated_rows = data[data['Content Rating'] == 'Unrated']
unrated_rows


# In[59]:


Not_Rated_rows = data[data['Content Rating'] == 'Not Rated']
Not_Rated_rows


# ### Dealing with the 'Score' column

# In[60]:


data['Score'].unique()


# In[61]:


# Chain str.replace operations for cleaning directly on data['Score']
data['Score'] = (
    data['Score'].str.replace(',', '', regex=True)
                 .str.replace(':', '.', regex=True)
                 .str.replace(r'\.\.', '.', regex=True)
                 .str.rstrip('.')
)

# Display the cleaned scores
print(data['Score'].unique())


# In[62]:


mapping = {
    '89f': 8.9,
    '9': 8.9,
    '08.9': 8.9,
    '++8.7': 8.7,
    '87e-0': 8.7,
    '86': 8.6
}

# Apply the mapping to the Score column
data['Score'] = data['Score'].replace(mapping)

data['Score'].unique()


# In[63]:


# Convert this column to float datatype
data['Score'] = data['Score'].astype(float)
data['Score'].head(4)


# In[64]:


data['Score'].unique()


# In[65]:


data.sample(5)


# In[66]:


data.info()


# In[67]:


data


# ## Analyzing the Cleaned Data

# 1. **Score vs. Income Correlation analysis** 
# 
# Let's examines the relationship between a movie's audience rating (Score) and its financial performance (income). The goal is to determine whether higher-rated movies tend to earn more revenue or if there's a disconnect between critical acclaim and box office success. This analysis helps in understanding the extent to which audience satisfaction influences a movie's profitability.

# #### Exploratory Data Analysis (EDA) for the Score vs. Income Correlation.

# - Summary Statistics for 'Score' and 'Income ($)'

# In[68]:


summary_stats = data[['Score', 'Income ($)']].describe()
print(summary_stats)


# - Visualizing Distributions

# In[69]:


import matplotlib.pyplot as plt

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

# In[70]:


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

# In[73]:


import matplotlib.pyplot as plt
import seaborn as sns

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

# In[76]:


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

# In[78]:


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

# ### Conclusion:
# The analysis highlights that certain genres, countries, and content ratings are associated with higher movie incomes. Action, Adventure, and Drama genres, as well as movies from New Zealand, USA, and France, generally perform better financially. Additionally, PG-13 rated movies have the widest appeal, leading to higher revenues. These insights can inform decisions in film production, marketing strategies, and distribution to maximize financial success.

# In[ ]:




