#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[3]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_df = pd.read_csv(file_to_load)

purchase_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[120]:


player_demo = purchase_data.loc[:, ["Gender", "SN", "Age"]]
player_demo = player_demo.drop_duplicates()
num_players = player_demo.count()[0]


players_df= pd.DataFrame({"Total Players": [num_players]})

players_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[153]:


items= len(purchase_df["Item Name"].unique())
average_price= purchase_df["Price"].mean()
purchases= purchase_df["SN"].count()
revenue= purchase_df["Price"].sum()


summary_df = pd.DataFrame({"Number of Unique Items": [items],
                          "Average Price": [average_price],
                          "Number of Purchases": [purchases],
                          "Total Revenue": [revenue]})
summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[162]:


gender_demos = purchase_df.groupby("Gender")
gender_count = gender_demos.nunique()["SN"] 
gender_percent = gender_count * 100 / num_players

gender_df = pd.DataFrame({"Total Count": gender_count, 
                                    "Percentage of Players": gender_percent})

gender_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[163]:


purchase_count= gender_demos["Purchase ID"].count()
purchase_price= gender_demos["Price"].mean()
purchase_total= gender_demos["Price"].sum()
per_person= purchase_total / gender_count


purchasing_df = pd.DataFrame({"Purchase Count": purchase_count, 
                                    "Average Purchase Price": purchase_price,
                                    "Average Purchase Value": purchase_total,
                                    "Avg Purchase Total per Person": per_person})

purchasing_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[167]:


bins_for_age = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
age_ranges = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_df["Age Group"] = pd.cut(purchase_df["Age"], bins_for_age, labels= age_ranges)


age_groups = purchase_df.groupby("Age Group")
age_count = age_groups["SN"].nunique()
age_percent = age_count * 100 / num_players


age_df = pd.DataFrame({"Total Count": age_count, "Percentage of Players": age_percent})
age_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[168]:


age_count = age_groups["Purchase ID"].count()
age_purchase_price = age_groups["Price"].mean()
age_total_purchase = age_groups["Price"].sum()
purchase_per_person = age_total_purchase / age_count


purchasing_by_age = pd.DataFrame({"Purchase Count": age_count,
                                 "Average Purchase Price": age_purchase_price,
                                 "Total Purchase Value": age_total_purchase,
                                 "Average Purchase Total per Person": purchase_per_person})

purchasing_by_age


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[171]:


sort_by_spender = purchase_df.groupby("SN")
spender_purchase_count = sort_by_spender["Purchase ID"].count()
avg_spent = sort_by_spender["Price"].mean()
spender_purchase_total = sort_by_spender["Price"].sum()


spenders_df = pd.DataFrame({"Purchase Count": spender_purchase_count,
                             "Average Purchase Price": avg_spent,
                             "Total Purchase Value": spender_purchase_total})

top_spenders= spenders_df.sort_values(["Total Purchase Value"], ascending=False)

top_spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[177]:


pop_items = purchase_df[["Item ID", "Item Name", "Price"]]
sort_by_items = pop_items.groupby(["Item ID","Item Name"])


pop_item_count = sort_by_items["Price"].count()
total_pop_item_purchase = (sort_by_items["Price"].sum())
pop_item_price = total_pop_item_purchase / pop_item_count


pop_items_df = pd.DataFrame({"Purchase Count": pop_item_count, 
                                   "Item Price": pop_item_price,
                                   "Total Purchase Value": total_pop_item_purchase})


most_pop_item = pop_items_df.sort_values(["Purchase Count"], ascending=False)

most_pop_item.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[179]:


profit_item = pop_items_df.sort_values(["Total Purchase Value"], ascending=False)

profit_item.head()


# In[ ]:




