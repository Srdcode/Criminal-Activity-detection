import streamlit as st
import mysql.connector
import trialerror

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

# Define a login function
def login(session_state):
  st.header("Login")
  username = st.text_input("Username")
  password = st.text_input("Password", type="password")
  if st.button("Login"):
    # Check if user exists in the database
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
      session_state.logged_in = True
      session_state.user = username
      st.success("Logged in successfully.")
      trialerror.main()  # call main function after successful login
    else:
      st.error("Invalid username or password. Create new account by sign up")
      # Create a sign-up form
      st.write("## Sign Up")
      new_username = st.text_input("Enter a new username:")
      new_password = st.text_input("Enter a new password:", type="password")
      if st.button("Sign Up"):
        if create_user(new_username, new_password):
            st.success("You have successfully signed up!")
        else:
            st.error("Sorry, there was an error signing you up.")


# Define function to create a new user
def create_user(username, password):
  # Check if user already exists in the database
  cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
  result = cursor.fetchone()
  if result:
      st.error("Username already exists.")
      return False
  else:
      # Insert the new user into the database
      cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
      db.commit()
      st.success("User created successfully.")
      return True
        
# # Close the database connection and cursor
# cursor.close()
# db.close()
