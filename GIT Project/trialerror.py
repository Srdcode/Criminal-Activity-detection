import streamlit as st
import mysql.connector
import streamlit_option_menu as som
from streamlit_lottie import st_lottie
import requests
import trialerror_predict
import trialerror_contact
import trialerror_home
import trialerror_about
import trialerror_signup

# st.set_page_config(page_title="Activity Prediction", page_icon=":tada:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_anim = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_go0eoxdr.json")


# Connect to the database
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Satya@123",
  database="labproject"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define a query to fetch all data from the users table
query = "SELECT * FROM users"

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

def main():
  # Set up session state
  session_state = st.session_state
  if not hasattr(session_state, "logged_in"):
    session_state.logged_in = False
    session_state.user = ""

  # If not logged in, show login form
  if not session_state.logged_in:
    trialerror_signup.login(session_state)
  # If logged in, show the main app
  else:
    st.title(f"Welcome, {session_state.user}! , You are now logged in.")
    u = ["Home", "Predict Activity", "About Project", "Contact", "Logout"]

    with st.sidebar:
        choice = som.option_menu(
            "Select an option", 
            u,
            icons=["house","upload","file-earmark-richtext-fill","envelope","box-arrow-right"],
        )
    with st.sidebar:
      st.header("You are under camera")
      st_lottie(lottie_anim,height=300,key="cameraanim")
    if choice == "Home":
      st.header("This is the Home page")
      trialerror_home.intro()
    elif choice == "Predict Activity":
      st.header("This is the Predict Activity page")
      trialerror_predict.predict_category()
    elif choice == "About Project":
      st.header("This is the About Project page")
      trialerror_about.docoments()
    elif choice == "Contact":
       st.header("This is the contact page")
       trialerror_contact.contact_us()
    elif choice == "Logout":
      session_state.logged_in = False
      session_state.user = ""
      st.write("You have been logged out.")


# Define a session state class to store the user login status
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Create a session state object and set logged_in to False
session_state = SessionState(logged_in=False)


if __name__ == "__main__":
  main()

# Close the database connection and cursor
cursor.close()
db.close()
