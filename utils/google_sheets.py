import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
import streamlit as st
import json

# Authenticate with Google Sheets
def connect_to_sheets():

    service_account_info = json.loads(st.secrets["gcp"]["service_account_json"])
    creds = Credentials.from_service_account_info(service_account_info, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])

    # Authenticate with gspread
    client = gspread.authorize(creds)
    
    # sheet = client.open_by_key(sheet_id)
    # worksheet = sheet.worksheet("Master")  # Change accordingly
    # data = worksheet.get(range_name)

    # return data
    
    # creds = Credentials.from_service_account_file("service_account.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
    # client = gspread.authorize(creds)
    return client

# Fetch data using Sheet ID and Range
def get_sheet_range(sheet_id, range_name):
    client = connect_to_sheets()
    sheet = client.open_by_key(sheet_id).values_get(range_name)  # Fetch data
    data = sheet.get("values", [])

    if not data:
        return pd.DataFrame()  # Return empty DataFrame if no data

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]  # Set the first row as column headers
    df = df[1:]  # Remove header row from data
    return df.reset_index(drop=True)
