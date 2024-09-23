
```markdown
# Excel Data Filter and Export Script

This script processes an Excel file named "Orders.xlsx" to filter and export specific order data based on predefined criteria.

## Requirements

### Python Environment
- Python 3.x installed on your machine.

### Required Libraries
Make sure to install the following libraries:

- **Pandas**: For data manipulation and filtering.
  ```bash
  pip install pandas
  ```
  
- **OpenPyXL**: For working with Excel files.
  ```bash
  pip install openpyxl
  ```

### Excel File
- An Excel file named **"Orders.xlsx"** should be located in the same directory as the script.
- The Excel file must contain the following columns:
  - `OrderID: `
  - `Package: `
  - `Department: `
  - `Phone: `
  - `Operation Confirmation: `
  - `Confirmation Date: `
  - `ETA: `
  - `Order Status: `
  - `Delivery Status: `

## Filtering Criteria
The code filters rows based on the following criteria:
- `Operation Confirmation:` is "Confirmed".
- `Order Status:` is "Sent to Delivery".
- `Delivery Status:` matches one of the following:
  - "Edit Completed"
  - "No Response"
  - "Pending Action"
  - "Pending Another Story"
  - "Pending Customer Confirmation"
  - "Pending Edit"
  - "Pending Phone Number"
  - "Customer Cancelled"

## Output Requirements
The filtered data is saved to a new Excel file with the following specifications:
- The file name format includes the date and time, e.g., "Sheet 09-22 12-30-45.xlsx".
- The new Excel sheet has:
  - Specific column widths.
  - The first row and first column frozen.
  - A black background with white font for all cells.
  - A light orange font color for the header row.
  - A gold font color for the "Package" column (C).
  - Cell height for the first row set to 100.
  - Borders applied to all cells.

## Running the Code
Execute the script in a terminal or command prompt where the current working directory contains the "Orders.xlsx" file.

```bash
python3 your_script_name.py
```

## Notes
- Feel free to adjust any styles or filtering criteria as needed based on specific requirements or preferences.
```
