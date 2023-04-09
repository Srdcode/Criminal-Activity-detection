import streamlit as st

import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Satya@123",
  database="labproject"
) 

# Create a cursor object to execute SQL queries
cursor = db.cursor()


# Load the model and categories
model = load_model('try1_model.h5')
# Define the list of categories
categories = ["Fighting","Kidnap"]
# Define the predict_category function
def predict_category():
    # File upload
    video_file = st.file_uploader("Upload video", type=["mp4", "avi"])
    predicted = st.button("predict")
    st.video(video_file)
    if predicted:

        if video_file is not None:
            # save the file to a local directory
            with open("temp.mp4", "wb") as f:
                f.write(video_file.getbuffer())

            # open the video file
            cap = cv2.VideoCapture("temp.mp4")

            frames = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.resize(frame, (224, 224))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Convert to RGB
                frame = frame.astype('float32') / 255.0 # Normalize pixel values
                frames.append(frame)
            cap.release()

            # remove the temporary file
            os.remove("temp.mp4")

            # Pad or truncate frames to desired length
            frames_per_sequence = 16
            if len(frames) < frames_per_sequence:
                frames.extend([np.zeros((224, 224, 3)) for _ in range(frames_per_sequence - len(frames))])
            else:
                frames = frames[:frames_per_sequence]

            # Convert frames to numpy array
            frames = np.array(frames)

            # Add batch dimension and change number of channels to 3
            frames = np.expand_dims(frames, axis=0)
            frames = np.expand_dims(frames,  axis=-1)

            # Make prediction
            predicted_probs = model.predict(frames)
            

            # Get the index of the category with the highest probability
            pred_idx = np.argmax(predicted_probs)
            predicted_category = categories[np.argmax(predicted_probs)]

            # Get the corresponding probability
            prob = predicted_probs[0][pred_idx]

            # Print the predicted category with the corresponding probability
            # st.write(f"Predicted category: {predicted_category}")
            # st.write(f"Probability: {prob:.2f}")

            # Use predict_category function to predict the activity
            # predicted_category = predict_category(file)
            st.success(f"Predicted activity: {predicted_category} , \n withAccuracy :  {prob}")

        # Insert prediction and video file location into database
        filename = video_file.name
        # Get the absolute path
        abs_path = os.path.abspath(filename)
        query = "INSERT INTO predictions (video_location, predicted_activity) VALUES (%s, %s)"
        data = (abs_path, predicted_category)
        cursor.execute(query, data)
        db.commit()

        # Read from database
        query = "SELECT video_location, predicted_activity FROM predictions"
        cursor.execute(query)
        results = cursor.fetchall()

        # Print the results
        for result in results:
            st.write(f"Video location: {result[0]},\n Predicted activity: {result[1]}")

# Close the database connection and cursor
cursor.close()
db.close()