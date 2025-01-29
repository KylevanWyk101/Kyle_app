import streamlit as st
import pandas as pd
from PIL import Image

# Title of the app
st.title("Researcher Profile Page")


# Add a section for profile photo upload
st.subheader("Upload Profile Photo")
profile_photo = st.file_uploader("Choose a profile photo", type=["jpg", "jpeg", "png"])

# Collect basic information
name = "Kyle van Wyk"
field = "Bioinformatics"
institution = "North-West Potchefstroom"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")



if profile_photo is not None:
    image = Image.open(profile_photo)
    st.image(image, caption="Profile Photo", use_column_width=True)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv", key="pub_upload")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")



# Add a contact section
st.header("Contact Information")
email = "Kylevanwyk101@gmail.com"
st.write(f"You can reach {name} at {email}.")