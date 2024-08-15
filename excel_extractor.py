import streamlit as st
import pandas as pd
import os

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
            # Create output directory if it doesn't exist
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)

            # Iterate through each sheet and download as CSV
            for sheet_name, sheet_data in df.items():
                # Get the filename from the first cell of the sheet
                filename = sheet_data.iloc[0, 0]
                # Add sheet name to filename to avoid overwriting
                filename = f"{filename}_{sheet_name}"
                csv_data = sheet_data.to_csv(index=False)
                csv_path = os.path.join(output_dir, f"{filename}.csv")
                with open(csv_path, "w") as f:
                    f.write(csv_data)
                st.success(f"Saved {sheet_name} as CSV to {csv_path}")
        elif download_format == "JSON":
            # Create output directory if it doesn't exist
            output_dir = "output"
            os.makedirs(output_dir, exist_ok=True)

            # Iterate through each sheet and download as JSON
            for sheet_name, sheet_data in df.items():
                # Get the filename from the first cell of the sheet
                filename = sheet_data.iloc[0, 0]
                # Add sheet name to filename to avoid overwriting
                filename = f"{filename}_{sheet_name}"
                json_data = sheet_data.to_json(orient="records")
                json_path = os.path.join(output_dir, f"{filename}.json")
                with open(json_path, "w") as f:
                    f.write(json_data)
                st.success(f"Saved {sheet_name} as JSON to {json_path}")
