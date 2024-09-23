Here’s a sample `README.md` for your two codes:

```markdown
# Orders Processing Scripts

This repository contains two Python scripts for automating order processing tasks in Excel. The first script retrieves order-related data from a Google Spreadsheet and filters it based on specific conditions. The second script processes an Excel file, extracts related orders based on the delivery status, and generates a formatted Excel report with custom styling.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Script 1: Google Spreadsheet Processing](#script-1-google-spreadsheet-processing)
  - [Description](#description)
  - [How to Run](#how-to-run)
- [Script 2: Excel Orders Processing](#script-2-excel-orders-processing)
  - [Description](#description-1)
  - [How to Run](#how-to-run-1)
- [Notes](#notes)

## Requirements

- Python 3.8+
- Google API Client (`google-auth`, `gspread`)
- Pandas
- Openpyxl
- gspread
- Google Cloud Project (for Google Spreadsheet API)
- `credentials.json` file from the Google Cloud Project

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Setup

1. Clone this repository and navigate to the project directory.
2. Ensure that Python 3.8 or higher is installed on your system.
3. Install the required Python packages by running:

```bash
pip install -r requirements.txt
```

4. If using the Google Sheets API, ensure that you have a `credentials.json` file from your Google Cloud Project. Place this file in the root directory of the project.
5. Ensure you have access to the Google Spreadsheet or Excel file you want to process.

## Script 1: Google Spreadsheet Processing

### Description

This script reads data from a Google Spreadsheet, processes it to find orders marked as `Pending Edit` with specific conditions, and outputs the count of such orders to another sheet. The script checks for confirmed orders and delivery statuses before proceeding.

### How to Run

1. Ensure you have the correct Google Spreadsheet ID and that your Google Cloud API credentials are correctly set up.
2. Run the script:

```bash
python google_spreadsheet_processing.py
```

3. The output will be written into the specified sheet within the same Google Spreadsheet.

### Script Breakdown

- **Read Google Spreadsheet**: The script connects to a Google Spreadsheet using the `gspread` library.
- **Filter Conditions**: It looks for orders in sheet 1 where:
  - Column `AJ` = "Confirmed"
  - Column `AN` = "Sent to Delivery"
- **Count Pending Edits**: The script counts rows that match these conditions and writes the count into sheet 2 of the spreadsheet.

## Script 2: Excel Orders Processing

### Description

This script processes an Excel file containing order information. It extracts orders with a specific `Chat Reference` and filters them based on the `Delivery Status`. The result is a formatted Excel report with combined data and customized styling, including merged cells and borders.

### How to Run

1. Place the Excel file you want to process in the same directory as the script, or specify the file path.
2. Run the script:

```bash
python excel_orders_processing.py
```

3. The script will output a new Excel file with a structured report. The file will be named starting with `PAS_` followed by the current date and time.

### Script Breakdown

- **Read Excel File**: The script reads the input Excel file containing orders using `pandas`.
- **Filter Orders**: It filters orders where:
  - The `Delivery Status` is `Pending Another Story`.
  - The `Chat Reference` is the same across multiple rows.
- **Generate Output**: The script creates a new Excel report with formatted output, merging cells for main orders and structuring related orders below the main ones. If no related orders are found, it inserts a separator (`▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬`).

## Notes

- Both scripts are designed for different types of order processing tasks. The Google Spreadsheet script works with online spreadsheets, while the Excel script works with local files.
- Make sure to update the file paths, spreadsheet IDs, and other parameters as needed before running the scripts.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation:

- The `README.md` covers the essential details of both scripts, including the required setup, how to run each script, and what each script does.
- It includes a `Requirements` section, where users can install the necessary Python libraries.
- The `How to Run` sections explain how to execute the scripts in their respective environments.
- Each script’s functionality is broken down clearly for ease of understanding.
