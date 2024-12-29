import streamlit as st
from datetime import datetime, timedelta

# Set page title and icon
st.set_page_config(page_title="Hair by [Your Name]", page_icon="💇‍♀️")

# Title
st.title("Hair by [Your Name]")

# Business Description
st.write("""
Welcome to **Hair by [Your Name]**, your go-to place for all hair styling needs. 
Here you can view our services, book an appointment, and get in touch with us.
""")

# Services Offered
st.header("Our Services")
services = {
    "Hair Cut": 25,
    "Hair Color": 60,
    "Highlights": 80,
    "Perm": 75,
    "Styling": 30,
    "Special Event Styling": 50
}

for service, price in services.items():
    st.markdown(f"- **{service}**: ${price}")

# Appointment Booking Form
st.header("Book an Appointment")

with st.form(key='appointment_form'):
    name = st.text_input("Your Name")
    service = st.selectbox("Select Service", list(services.keys()))
    date = st.date_input("Appointment Date", min_value=datetime.now().date() + timedelta(days=1))
    time = st.time_input("Time")
    submit_button = st.form_submit_button(label='Book Appointment')

    if submit_button:
        st.success(f"Appointment for {service} booked for {name} on {date} at {time}!")

# Contact Information
st.header("Contact Us")
st.markdown("""
- **Email:** yourname@example.com
- **Phone:** (123) 456-7890
- **Address:** 123 Hair Stylist Lane, City, State, ZIP
""")

# About Us
st.subheader("About [Your Name]")
st.write("""
[Your Name] has been in the hair styling business for over [X] years, providing top-notch hair services. 
Our salon is dedicated to ensuring every client leaves looking and feeling their best.
""")

# Footer
st.markdown("---")
st.write("© 2023 Hair by [Your Name]. All rights reserved.")
```
