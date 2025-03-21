import streamlit as st
from pages import dashboard, current, listitems, entries

st.set_page_config(page_title="See Saw", layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(["Dashboard", "Current", "Listitems", "Entries"])

with tab1:
    dashboard.show()
with tab2:
    current.show()
with tab3:
    listitems.show()
with tab4:
    entries.show()