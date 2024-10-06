# Order Processing Script

This Python script processes an Excel file named `Orders.xlsx` to filter and export order data based on specific criteria. The resulting data is formatted and saved in a new Excel file, providing an easy-to-read summary of relevant orders.

## Features

- Filters orders based on:
  - **Operation Confirmation**: Confirmed
  - **Order Status**: Sent to Delivery
  - **Delivery Status**: No Response
- Groups orders by phone number.
- Merges phone number cells in the output for clarity.
- Formats the output with borders and background colors for better readability.
- Saves the output with a timestamp in the filename.

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `openpyxl`
  
You can install the required libraries using pip:

```bash
pip install pandas openpyxl
