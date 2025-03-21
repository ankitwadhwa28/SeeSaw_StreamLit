import streamlit as st
from utils.google_sheets import get_sheet_range

def show():
    st.title("Current Items")

    # Google Sheets Configuration
    SHEET_ID = '1gAOpImxyt_anGrfeK6x2P9DTmFEaMVfkZ_re9DZVacs'  # Replace with your actual Sheet ID
    RANGE_NAME = 'Master!C25:U48'

    # Fetch data
    try:
        df = get_sheet_range(SHEET_ID, RANGE_NAME)
        if df.empty:
            st.warning("No data found in the specified range.")
        else:
            st.dataframe(df)  # Display the data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
