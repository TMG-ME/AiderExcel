# Excel Data Extractor

This simple web application allows you to easily extract data from all worksheets within an Excel file. It provides a user-friendly interface to upload your Excel file and view the extracted data in a clear and organized format. You can also download all the extracted data as a CSV file.

## Features

*   **Handles multiple Excel file formats:** Supports both `.xls` and `.xlsx` files.
*   **Extracts data from all worksheets:** Reads and processes data from every sheet within the uploaded Excel file.
*   **Preserves data structure:** Maintains the original column headers and row order.
*   **Displays data in a table:** Presents the extracted data in an easy-to-read table format.
*   **Downloads data as CSV:** Provides a button to download all extracted data combined into a single CSV file.
*   **Error handling:** Includes basic error handling to gracefully manage invalid or corrupted files.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone [invalid URL removed]
    cd excel-data-extractor
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run excel_extractor.py
    ```

4.  **Open in your browser:** The application will open in your default web browser.

5.  **Upload your Excel file:** Click on the "Choose an Excel file" button or drag and drop your file into the designated area.

6.  **View the extracted data:** The data from each worksheet will be displayed in separate tables.

7.  **Download the data (optional):** Click the "Download All Data as CSV" button to download all the extracted data as a CSV file.

## Requirements

*   Python 3.x
*   pandas
*   streamlit

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
