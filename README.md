# CaloriePredictor
This project consists in creating a machine learning algorithm to predict calorie expenditure in a workout session as well as the amount of calories needed to recover from the workout based on age, gender, body temperature during workout, heart rate intensity, workout duration, among other factors.

This is a work in progress and will be updated on a regular basis.


## Data Preprocessing: 
 - For this project, We are using a Kaggle dataset composed of 3 CSV files: Calories.csv, Intake.csv, Exercise.csv
 - Jupyter Notebook has been used to load and preprocess the data, as well as train the model.
 - Numpy and Pandas have been used for data preprocessing.
 - Matplotlib and Seaborn were used for dataset visualization
 - Finally, a Regressor model was used to train the model with good accuracy. With algorithms such as XGBoost, Random Forest, Decision Tree, and Linear Regression
 - XAI techniques of Shapley Analysis and LIME were implemented in order to understand the feature influence on the predicted values
 - Random Forest showed the best results and thus was used as the trained model for the WebApp

## User Interface and Model Deployment:
 - Streamlit is used to build a user-friendly interface with which the users can interact with the model
 - In the first phase, Streamlit Community Cloud will be used to deploy the WebApp
 - In later phase, GCP Kubernetes Engine will be used to deploy the WebApp in a container enviroment
