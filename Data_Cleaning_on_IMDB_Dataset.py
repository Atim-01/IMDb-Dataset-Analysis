#!/usr/bin/env python
# coding: utf-8

# ### Data Cleaning Process

# In[4]:


import pandas as pd


# In[5]:


file_path = 'C:/Users/Administrator/Downloads/messy_IMDB_dataset.csv'

# Load the Data
try:
    # Read the CSV file
    data = pd.read_csv(file_path, delimiter=';', encoding='latin1', on_bad_lines='skip')
except Exception as e:
    print(f"Error reading the file: {e}")


# In[6]:


data.sample(4)


# In[7]:


data.info()


# In[8]:


# Clean and process the DataFrame as needed
data.columns = data.columns.str.strip()


# In[9]:


data


# ### Dealing with the 'Unnamed: 8' column

# In[10]:


data['Unnamed: 8'].isnull().sum()


# In[11]:


data['Unnamed: 8'].unique()


# In[12]:


# All its values are null, hence this column is not needful. I will drop it
data.drop(columns=['Unnamed: 8'], inplace=True)


# In[13]:


data.sample(3)


# ### Dealing with the 'Income' column

# In[14]:


# I want to change the column content to float data type
data["Income"].unique()


# In[15]:


data['Income'] = data['Income'].str.replace('$', '', regex=True)
data.sample(3)


# In[16]:


data['Income'] = data['Income'].str.replace('o', '0', regex=True)
data.sample(3)


# In[17]:


data['Income'].str.strip()


# In[18]:


data['Income'] = data['Income'].str.replace(',', '', regex=True)
data['Income'].sample(3)


# In[19]:


data['Income'] = data['Income'].astype(float)  # Changing the data type


# In[20]:


data['Income'].info()


# In[21]:


data.sample(4)


# In[22]:


data['Income'].unique()


# In[23]:


pd.set_option('display.float_format', lambda x: '%.2f' % x) # I dont want it to display in scientific form


# ### I want to rename some of the column headers

# In[24]:


data = data.rename(columns={'Original titlÊ': 'Original title', 'Genrë¨': 'Genre', 'Duration':'Duration (mins)', 'Income':'Income ($)'})


# In[25]:


data.sample(3)


# ### Dealing with the 'Release year' column

# In[26]:


invalid_dates = data[data['Release year'].isna()]
invalid_dates


# In[27]:


data['Release year'].sample(3)


# In[28]:


data['Release year'] = pd.to_datetime(data['Release year'], dayfirst=True, errors='coerce')


# In[29]:


data['Release year'].info()


# In[30]:


data['Release year'].head(2)


# ### Dealing with the 'Duration (mins)' column

# In[31]:


data['Duration (mins)'].unique()


# In[32]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('c', '', regex=True)


# In[33]:


data['Duration (mins)'].unique()


# In[34]:


specific_date = 'Not Appliable'  # Example specific date to search for

specific_rows = data[data['Duration (mins)'] == specific_date]
specific_rows


# In[35]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('Not Appliable', 'nan', regex=True)


# In[36]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace('-', 'nan', regex=True)


# In[37]:


data['Duration (mins)'].unique()


# In[38]:


data['Duration (mins)'] = data['Duration (mins)'].str.replace(' ', 'nan', regex=True)
data['Duration (mins)'] = data['Duration (mins)'].str.replace('Nan', 'nan', regex=True)


# In[39]:


data['Duration (mins)'].unique()


# In[40]:


data['Duration (mins)'] = data['Duration (mins)'].astype(float)  # Changing the data type


# In[41]:


data['Duration (mins)'].info()


# In[42]:


data.sample(5)


# In[43]:


data.info()


# ### Dealing with 'Votes' column

# In[44]:


data['Votes'].unique()


# In[45]:


data['Votes'] = data['Votes'].str.replace('.', '', regex=True).astype(float)  # Changing the data type


# In[46]:


data['Votes'].sample(5)


# In[47]:


data.info()


# ### Dealing with the 'Country' column

# In[48]:


data['Country'].unique()


# In[49]:


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


# In[50]:


data['Original title'].sample(5)


# ### Others

# In[51]:


data.iloc[13] #Noticed this row with all null values. Let's confirm 


# In[52]:


rows_with_nan = data[data.isna().all(axis=1)] # Let's see if there are other like it
rows_with_nan


# In[53]:


data = data.drop(index=13)


# In[54]:


data.head(15) 


# ### Dealing with the "Content Rating" column

# In[55]:


data['Content Rating'].isnull().sum()


# In[56]:


data['Content Rating'].unique()


# In[57]:


# I want to see how many rows have the 'Approved' has the value for this column
approved_rows = data[data['Content Rating'] == 'Approved']
approved_rows


# In[58]:


# Changing 'Approved' to 'G'
data['Content Rating'] = data['Content Rating'].str.replace('Approved', 'G', regex=True)


# In[59]:


data['Content Rating'].unique()


# In[60]:


unrated_rows = data[data['Content Rating'] == 'Unrated']
unrated_rows


# In[61]:


Not_Rated_rows = data[data['Content Rating'] == 'Not Rated']
Not_Rated_rows


# ### Dealing with the 'Score' column

# In[62]:


data['Score'].unique()


# In[63]:


# Chain str.replace operations for cleaning directly on data['Score']
data['Score'] = (
    data['Score'].str.replace(',', '', regex=True)
                 .str.replace(':', '.', regex=True)
                 .str.replace(r'\.\.', '.', regex=True)
                 .str.rstrip('.')
)

# Display the cleaned scores
print(data['Score'].unique())


# In[64]:


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


# In[65]:


# Convert this column to float datatype
data['Score'] = data['Score'].astype(float)
data['Score'].head(4)


# In[66]:


data['Score'].unique()


# In[67]:


data.sample(5)


# In[68]:


data.info()


# In[69]:


data


# In[70]:


data.to_csv("cleaned_IMDb_dataset.csv", index = False)


# In[ ]:




