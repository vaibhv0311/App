import numpy as np
import pickle
import requests
import streamlit_lottie as st_lottie
import streamlit as st
import datetime
from datetime import date


# Loading the saved model
loaded_model1 = pickle.load(open(r'C:\Users\Admin\Desktop\Major\App\btrained_model.pkl', 'rb'))
loaded_model2 = pickle.load(open(r'C:\Users\Admin\Desktop\Major\App\itrained_model.pkl', 'rb'))


def burnt_calorie_prediction(user_input):

    # Transforming user input data into a numpy array
    user_input_array = np.asarray(user_input)

    # We need to reshape the array so that we can use it in our model
    user_input_reshaped = user_input_array.reshape(1,-1)

    # Calculating prediction based on user input

    burnt_user_input_prediction = loaded_model1.predict(user_input_reshaped)


    return burnt_user_input_prediction

def intake_calorie_prediction(user_input):

    # Transforming user input data into a numpy array
    user_input_array = np.asarray(user_input)

    # We need to reshape the array so that we can use it in our model
    user_input_reshaped = user_input_array.reshape(1,-1)

    # Calculating prediction based on user input

    intake_user_input_prediction = loaded_model2.predict(user_input_reshaped)


    return intake_user_input_prediction

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Loading Lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    st.set_page_config(page_title="Calories Predictor", page_icon=":flexed bicep:", layout="wide")

    local_css("style/style.css")
    lottie_workout = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_8xkaygbw.json")
    lottie_predict = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_kit9njnq.json")
    
    # ----------HEADER SECTION----------
    with st.container():
        st.subheader("Hi, Group 194 this side! :wave:")
        st.title("Intelligent Calorie Intake and Burn Prediction")
        st.write(
            """
            This is a Machine Learning based Calorie Predictor app that can predict both the calories 
            that you need to burn and take to have a healthy lifestyle created by our team Group 194
            - Vaibhav Sharma, Naman Mittal, Nupur Bhardwaj, Priyanshi Chauhan
            
            """
        )
        

    #-------WHAT IT DOES---------------
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What it is")
            st.write("##")
            st.write(
                """
                - This project aims to predict calories burnt by the user based on their body measurements
                and their workout routine. 
                - It takes in all these factors into consideration and predicts the amount of
                calories that the person burnt during the workout and needs to take on a daily basis in order to maintain a healthy lifestyle.
                - On the research side of things, Explanable AI was implemented in order to understand the influence of the factors involved, i.e. our weight, height, duration of workout and such. 
                """
            )
        with right_column:
            st_lottie.st_lottie(lottie_workout, height=300, key='workout')
            
    #-----MAIN FORM---------
    with st.container():
        # Giving a title
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("Predict your Calories!")

            # Getting the inputs from the user
            Gender = st.selectbox('Select your gender at birth', ["Male","Female"])
            if Gender == "Male":
                Gender = 0
            else:
                Gender = 1

            Age_input = st.date_input("Type your Birthday",min_value=datetime.date(1930, 1, 1),max_value=date.today())
            today = date.today()
            Age = float((today - Age_input)/datetime.timedelta(days=365))

            Height = st.number_input("Type your Height in cm")
            Weight = st.number_input("Type your Weight in kg")
            Duration = st.slider('Select your Workout Duration in minutes', 1, 150, 1)
            HeartRate = st.slider("Select your average Heart Rate in beats per minute",50, 190, 1)
            BodyTemperature = st.number_input("Body Temperature in Celsius")

            # Code for prediction
            bprediction = ""
            iprediction = ""

            # Creating a button for prediction
            
                
        with right_column:
            st_lottie.st_lottie(lottie_predict, height=300, key='predict')
            st.write("######")
            with st.container():
                left_column,centre_column,right_column=st.columns([0.3,2,0.3])
                with centre_column:
                    if st.button("Predict!", key='button_predict'):
                        bprediction = round(float(burnt_calorie_prediction([Gender, Age, Height, Weight, Duration, HeartRate, BodyTemperature])[0]),2)   
                        iprediction = round(float(intake_calorie_prediction([Gender, Age, Height, Weight, Duration, HeartRate, BodyTemperature])[0]),2)
                        st.success(f"You burnt {bprediction} calories in this workout session!", icon="✅")
                        st.success(f"You need to have {iprediction} calories today for the recovery!", icon="✅")


    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Us!")
        st.write("##")
        st.write("""
        We would love to hear your suggestions on the application and would love to resolve your doubts!
        """)
        st.write("###")
        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sharma.vaibhav0311@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

if __name__ == "__main__":
    main()