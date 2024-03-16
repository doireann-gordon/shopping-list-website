import streamlit as st
import ast
import pandas as pd

# setup
st.set_page_config(layout = "wide",page_title = "Menu")
st.title = "Menu"

# Load the data from a CSV file
file_path = "./data/meals.csv"
df = pd.read_csv(file_path)
df = df.astype({"Meal":'category', "Ingredients":'str', "Item type":'str'})


#meal_options = pd.unique(df['Meal'])
# Checkbox for meal selection
#selected_meals = st.multiselect('Select Meals:', meal_options)
selected_meals = st.multiselect('Select Meals:', df['Meal'].cat.categories)

# Filter dataframe based on selected meals
filtered_df = df[df['Meal'].isin(selected_meals)]

# # Display ingredients
# if not filtered_df.empty:
#     st.subheader('Selected Ingredients:')
#     for ingredients in filtered_df['Ingredients']:
#         st.write((ingredients))
# else:
#     st.warning('Please select meals to see ingredients.')

# Display fresh ingredients
if not filtered_df.empty:
    st.subheader('Fresh ingredients')
    fresh = filtered_df[filtered_df['Item type'] == "Fresh"]
    for ingredients in fresh['Ingredients']:
        st.write((ingredients))
else:
    st.warning('Please select meals with fresh ingredients.')

# Display pantry ingredients
if not filtered_df.empty:
    st.subheader('Pantry ingredients')
    pantry = filtered_df[filtered_df['Item type'] == "Pantry"]
    for ingredients in pantry['Ingredients']:
        st.write((ingredients))
else:
    st.warning('Please select a meal with pantry ingredients.')

