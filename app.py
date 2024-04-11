import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the model and data
pipe = joblib.load('pipe.pkl')
df = pd.read_pickle('df.pkl')

# Divide the layout into two columns
col1, col2 = st.columns(2)

# Use the first column to display the title
with col2:
    st.title("Laptop Nest")

# Use the second column to display the image
with col1:
    image_path = 'logo_1.png'  # Update this to your image path
    # Display the image with a specified width
    st.image(image_path, width=200)

# Type of laptop
laptop_type = st.selectbox('Type', ["Notebook", "Gaming", "Portable", "Touch Screen"])

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input('Weight of the Laptop')

# Screen size
screen_size = st.number_input('Screen Size')

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# Button to trigger prediction
if st.button('Predict Price'):

    # Check if any of the required fields are empty
    if weight == 0:
        st.title("Weight!")
    elif screen_size == 0:
        st.title("Screen Size!") 
    elif hdd == 0:
        st.title("HDD!")

    # Proceed with prediction if all required fields are filled
    if hdd != 0 and weight != 0 and screen_size != 0:
        query_df = pd.DataFrame({
            'Ram': [ram],
            'HDD': [hdd],
            'Inches': [screen_size],
            'Weight': [weight],
            'TypeName': [laptop_type]
        })

        # Make prediction
        prediction = np.exp(pipe.predict(query_df))
        
        # Displaying the Predictions
        st.title(f"Predictions: {prediction[0]}")
        
        # Display detailed prediction
        st.title(f"{prediction[1]}: \t\t INR {round(prediction[2], 2)}")
