import streamlit as st
import pandas as pd

st.title("Excel Data Extractor")

# File upload
uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

if uploaded_file is not None:
    # Read Excel file using pandas
    try:
        df = pd.read_excel(uploaded_file, sheet_name=None)  # Read all sheets
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
    else:
        # Display extracted data
        st.write("## Extracted Data:")
        for sheet_name, sheet_data in df.items():
            st.write(f"### {sheet_name}")
            st.dataframe(sheet_data)

        # Download options
        st.write("## Download Options:")
        download_format = st.selectbox("Choose download format", ["CSV", "JSON"])
        if download_format == "CSV":
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="Download as CSV",
                data=csv_data,
                file_name="extracted_data.csv",
                mime="text/csv",
            )
        elif download_format == "JSON":
            json_data = df.to_json(orient="records")
            st.download_button(
                label="Download as JSON",
                data=json_data,
                file_name="extracted_data.json",
                mime="application/json",
            )
