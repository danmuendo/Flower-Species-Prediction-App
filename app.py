import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('flower_species_model.pkl')

# Function to make predictions
def predict_species(size, fragrance, height_cm):
    data = pd.DataFrame([[size, fragrance, height_cm]], columns=['size', 'fragrance', 'height_cm'])
    prediction = model.predict(data)
    return prediction[0]

# Streamlit app
st.title('Flower Species Prediction App')

st.write('Enter the characteristics of the flower:')

size = st.selectbox('Size', ['small', 'medium', 'large'])
fragrance = st.selectbox('Fragrance', ['none', 'mild', 'high'])
height_cm = st.number_input('Height (cm)', min_value=0.0)

if st.button('Predict'):
    size_encoded = 2 if size == 'small' else 1 if size == 'medium' else 0
    fragrance_encoded = 1 if fragrance == 'none' else 0 if fragrance == 'mild' else 2
    prediction = predict_species(size_encoded, fragrance_encoded, height_cm)
    st.write(f'The predicted species is: {prediction}')
