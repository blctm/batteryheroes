import streamlit as st

# Print all keys inside the secrets
st.write("Secrets Keys:", list(st.secrets["gcp_service_account"].keys()))
