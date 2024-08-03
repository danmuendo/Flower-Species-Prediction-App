# Flower Species Prediction App

This project is a Streamlit web application that predicts the species of a flower based on its characteristics such as size, fragrance, and height. The prediction model is trained using a dataset containing information about different flower species.


## Features
User-friendly Interface: Simple web interface to input flower characteristics.
Real-time Prediction: Predicts the species of a flower instantly upon input.
Encodings: Properly encoded categorical inputs for size and fragrance.

## Dataset
The dataset used for training the model contains the following columns:

##### species: The type of flower.
##### size: The size of the flower, encoded as:
    2: Small
    1: Medium
    0: Large
###### fragrance: The fragrance level, encoded as:
    1: None
    0: Mild
    2: High
##### height_cm: The height of the flower in centimeters.

## Installation

#### Prerequisites
Python 3.x
Streamlit
Pandas
Joblib
scikit-learn

#### Step-by-step Installation

1. Clone the Repository:

git clone https://github.com/your-username/flower-species-prediction.git
cd flower-species-prediction


2. Install Required Packages:
Ensure you have all necessary packages by installing them


## Usage
To run the app locally, execute the following command in your terminal:

streamlit run app.py

## Using the App

Size: Select the size of the flower (small, medium, large).

Fragrance: Select the fragrance level (none, mild, high).

Height (cm): Enter the height of the flower in centimeters.

After running the above command, the app will open in a web browser window, allowing you to input the features and predict the species.

## Model
The model is a Random Forest Classifier trained to predict flower species based on encoded input features. It has been trained and evaluated using standard machine learning practices and can be retrained with updated data as needed.

## Model Training
The model is trained using a Random Forest Classifier from scikit-learn. The features used for training include size, fragrance, and height_cm.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.

## Steps to Contribute
Fork the repository.

Create a new branch for your feature: git checkout -b feature-name

Commit your changes: git commit -m 'Add new feature'

Push to the branch: git push origin feature-name

Open a pull request.
