import streamlit as st
import webbrowser

def contact_us():
    st.title(f"contact us here:e-mail:")
    # Define the recipient email address
    recipient = "srd2802@gmail.com"
    # Add a way to contact us directly
    st.write('If you encounter any issues with the form or need additional assistance, please email us at srd2802@gmail.com')

    # Construct the mailto: URL
    subject = "Contact Form Submission"
    body = "Please enter your message here."
    mailto_url = f"mailto:{recipient}?subject={subject}&body={body}"
    # Open the user's default email client
    #  import webbrowser
    # webbrowser.open(mailto_url)



 

