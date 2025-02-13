import streamlit as st

# Check if Streamlit Secrets are loading correctly
if "gcp_service_account" in st.secrets:
    stored_keys = list(st.secrets["gcp_service_account"].keys())
    st.write("✅ Stored Keys in Secrets:", stored_keys)

    # Check if 'private_key' exists
    if "private_key" in stored_keys:
        st.write("✅ 'private_key' is available!")
    else:
        st.error("❌ 'private_key' is missing! Check Streamlit Secrets.")
        st.stop()  # Stop execution if private_key is missing
else:
    st.error("❌ 'gcp_service_account' is missing! Check Streamlit Secrets.")
    st.stop()
