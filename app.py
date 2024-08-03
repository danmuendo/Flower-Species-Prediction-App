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

# Set a theme for the app
st.set_page_config(
    page_title="Flower Species Prediction",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        color: #2C3E50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        color: #34495E;
        font-size: 24px;
        font-weight: normal;
    }
    .widget {
        margin-top: 20px;
    }
    .predict-button {
        background-color: #1ABC9C;
        color: white;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        margin-top: 20px;
        border-radius: 5px;
    }
    .predict-button:hover {
        background-color: #16A085;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
        background-color: #f0f2f6;
        color: #34495E;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle with custom styles
st.markdown('<h1 class="title">Flower Species Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Enter the characteristics of the flower below:</h2>', unsafe_allow_html=True)

# User input widgets with some spacing and custom styles
st.markdown('<div class="widget">', unsafe_allow_html=True)
size = st.selectbox('Size', ['small', 'medium', 'large'], key='size')
fragrance = st.selectbox('Fragrance', ['none', 'mild', 'high'], key='fragrance')
height_cm = st.number_input('Height (cm)', min_value=0.0, step=0.1, key='height')
st.markdown('</div>', unsafe_allow_html=True)

# Predict button with custom style
if st.button('Predict', key='predict', help="Click to predict the flower species"):
    size_encoded = 2 if size == 'small' else 1 if size == 'medium' else 0
    fragrance_encoded = 1 if fragrance == 'none' else 0 if fragrance == 'mild' else 2
    prediction = predict_species(size_encoded, fragrance_encoded, height_cm)
    st.success(f'The predicted species is: **{prediction}**')

# Footer with some information
st.markdown('<div class="footer">Developed by Dan | Powered by Streamlit</div>', unsafe_allow_html=True)
