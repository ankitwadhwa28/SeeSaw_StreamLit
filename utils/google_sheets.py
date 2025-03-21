import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Authenticate with Google Sheets
def connect_to_sheets():
    creds = Credentials.from_service_account_file("service_account.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(creds)
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
