import streamlit as st
import boto3
import json

# Initialize AWS clients
sfn_client = boto3.client('stepfunctions')

# Constants
STEP_FUNCTION_ARN = 'YOUR_STEP_FUNCTION_ARN'
SNS_TOPIC_ARN = 'YOUR_SNS_TOPIC_ARN'

def get_execution_status(execution_arn):
    response = sfn_client.describe_execution(executionArn=execution_arn)
    return response['status'], response['output']

def fetch_notifications():
    # Placeholder for actual notification fetching logic
    return ["Last pipeline execution: Success", "Last pipeline execution: Failed"]

st.title("E-Commerce ETL Pipeline Status")

if st.button("Check Pipeline Status"):
    execution_arn = st.text_input("Enter the Step Function Execution ARN:")
    if execution_arn:
        status, output = get_execution_status(execution_arn)
        st.write(f"Execution Status: **{status}**")
        if output:
            st.write("Output:")
            st.json(json.loads(output))
    else:
        st.warning("Please enter a valid Step Function Execution ARN.")

st.subheader("Notifications")
notifications = fetch_notifications()
for notification in notifications:
    st.write(notification)

if st.button("Start ETL Pipeline"):
    # Logic to start the Step Function
    st.success("ETL Pipeline has been initiated!")

st.sidebar.header("Info")
st.sidebar.write("This application allows you to check the status of the ETL pipeline and view recent notifications.")
