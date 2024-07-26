import streamlit as st

# Set the title of the app
st.title("IEEE Resonate")

# Add a description
st.write("""
Welcome to the IEEE Resonate app! This application is designed to provide resources,
updates, and interactive content for IEEE members and enthusiasts.
""")

# Add a sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the options below to navigate through the app.")

# Add a selectbox in the sidebar for navigation
option = st.sidebar.selectbox(
    'Choose a page',
    ('Home', 'Events', 'Resources', 'Contact')
)

# Define content for each page
if option == 'Home':
    st.header("Home")
    st.write("This is the home page of the IEEE Resonate app.")

elif option == 'Events':
    st.header("Events")
    st.write("Here you can find information about upcoming IEEE events.")

elif option == 'Resources':
    st.header("Resources")
    st.write("Access various resources related to IEEE activities and projects.")

elif option == 'Contact':
    st.header("Contact")
    st.write("Get in touch with IEEE representatives through this page.")

# Add a footer
st.write("© 2024 IEEE Resonate")
