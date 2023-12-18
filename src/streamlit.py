import streamlit as st
from Summarizer import Summarizer

# Streamlit app title
st.title("YouTube Video Summarizer")

# Input field for the YouTube video link
video_link = st.text_input("Enter YouTube Video Link:")

# Check if the link is provided
if video_link:
    # Button to trigger the summary generation
    if st.button("Generate Summary"):
        try:
            # Create an instance of the model
            model = Summarizer()

            # Call the generate_summary method
            summary = model.generate_summary(video_link)

            # Display the generated summary
            st.subheader("Generated Summary:")
            st.write(summary)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

link = '<div style="position:fixed; bottom:0; left:0; width:100%; background-color:#f1f1f1; text-align:center; padding:10px;">Made by <a href="https://github.com/Niez-Gharbi" target="_blank">Niez Gharbi</a></div>'
st.markdown(link, unsafe_allow_html=True)