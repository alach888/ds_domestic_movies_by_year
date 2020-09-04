#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[60]:


start_year = 1977
end_year = 2020
years = list(range(start_year, end_year+1))
year_dfs = {}

#get the information for each year
for year in years:
    dfs = pd.read_html('https://www.boxofficemojo.com/year/'+str(year)+'/?grossesOption=calendarGrosses')
    df = dfs[0]
    year_dfs[year] = df
    


# In[61]:


print(year_dfs[2020].columns)
#Remove columns without any data in them
#Remove rank column
for year in years:
    year_dfs[year].drop(['Rank', 'Genre', 'Budget', 'Running Time', 'Estimated'], axis=1, inplace=True)
#after removing columns
print(year_dfs[2020].columns)


# In[74]:


pd.set_option('max_colwidth',5)
#add column for year
for year in years:
    year_dfs[year]['Year'] = year
#combine all the dataframes from each year into one
combined_df = pd.concat(year_dfs.values(), ignore_index=True)

#remove $ from Gross and Total Gross
#add column for release month
#change Distributor null values from '-' to 'N/A'

