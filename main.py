import os
import pandas as pd
import streamlit as st
from pandasai import Agent

# Set the API key for pandasai
os.environ["PANDASAI_API_KEY"] = "$2a$10$qQ7Jcb.arA15LKzos5vpx.wZZ07dghA8W6jOUnyiPW35zGT5vNnqO"

# Function to load the CSV file
def load_csv(file):
    df = pd.read_csv(file)
    return df

# Streamlit app
st.title("Data Analysis with PandasAI")

# File upload option
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the CSV file
    data = load_csv(uploaded_file)

    # Display the DataFrame
    st.write("### Uploaded Data")
    st.write(data)

    # Create pandasai agent
    agent = Agent(data)

    # User input for the question
    user_question = st.text_input("Ask a question about the data")

    if user_question:
        # Get the answer from pandasai
        result = agent.chat(user_question)

        # Path to the chart image
        chart_path = "/home/runner/ChatCsv/exports/charts/temp_chart.png"

        # Check if the chart image exists
        if os.path.exists(chart_path):
            # Display the plot
            st.write("### Plot")
            st.image(chart_path)
            # Optionally, remove the file after displaying to avoid showing the old plot for new questions
            os.remove(chart_path)
        else:
            # Display the result
            st.write("### Answer")
            st.write(result)
else:
    st.write("Please upload a CSV file to proceed.")
