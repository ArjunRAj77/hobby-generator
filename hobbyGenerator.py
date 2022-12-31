import pandas as pd
import random
import streamlit as st

# Load the Excel file into a Pandas dataframe
df = pd.read_csv('hobbylist.csv')
st.title("Hobby Generator")
st.write(" 🕵️ Want a new hobby this year ?") 
st.write(" Hop on to the hobby generator and randomly pick a hobby!😎 ")
# Create a dropdown menu for selecting a hobby category
category = st.sidebar.selectbox('Select a category:', ['All'] + sorted(set(df['Type'])))

if st.button('Generate hobby 🧙‍♂️ '):
    # If the user selects a specific category, filter the dataframe to include only those hobbies in that category
    if category != 'All':
        df = df[df['Type'] == category]
    # Select a random index from the dataframe
    index = random.randint(0, df.shape[0] - 1)
    # Access the row at the selected index
    row = df.iloc[index]
    # Extract the hobby name from the row
    hobby = row['Hobby-name']
    st.write("🤩 Your randomly generated hobby is : ")
    st.markdown(f"**{hobby}**")
