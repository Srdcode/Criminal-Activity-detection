import streamlit as st
st.set_page_config(page_title="Activity Prediction", page_icon=":tada:")
def intro():
    # Define the page title and description
    st.title("Welcome to my Web App! :derelict_house_building:")

    # Add a header for the app description
    st.header("About the Web App")
    st.write("This web app is designed to help you detect the suspicious activity. It was created using Streamlit, a Python framework for building data apps.")

    # Add a header for the model description
    st.header("About the Model")
    st.write("The model used in this web app is a activity detector. It was trained on kaggle data set and has achieved an accuracy of [insert accuracy here].")

    # Add any additional content you'd like to include on the home page
