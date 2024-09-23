```markdown
# Order Processing Script

This script processes an Excel file named **"Orders.xlsx"** to filter and organize order data based on specific criteria. The output is saved to a new Excel file with a timestamp.

## Requirements

1. **Python Environment**:
   - Python 3.x installed on your machine.

2. **Required Libraries**:
   Ensure you have the following libraries installed:
   - **Pandas**: For data manipulation and filtering.
   ```bash
   pip install pandas
   ```
   - **OpenPyXL**: For working with Excel files.
   ```bash
   pip install openpyxl
   ```

3. **Excel File**:
   - An Excel file named **"Orders.xlsx"** should be located in the same directory as the script.
   - The Excel file must contain the following columns:
     - `OrderID:`
     - `Chat Reference:`
     - `Delivery Status:`
     - `Phone:`
     - `Department:`
     - `Package:`

## Functionality

The script performs the following tasks:

- Reads the input Excel file and ensures that column names are stripped of extra spaces.
- Filters orders that have the `Delivery Status` set to **"Pending Another Story"**.
- Groups the filtered orders by `Chat Reference` and prepares a list of merged Order IDs.
- Outputs related orders for each `Chat Reference` and saves the data to a new Excel file.

## Output

The filtered data is saved to a new Excel file with:
- The filename format as **"PAS MM.DD-HH.MM.SS.xlsx"**.
- The following columns:
  - Merged `Order IDs`
  - `Delivery Status`
  - `Phone`
  - `Department`
  - `Package`
- The first row is frozen for better readability.
- Borders, colors, and alignment styles are applied for improved visual formatting.

## Running the Code

To execute the script, run the following command in your terminal or command prompt:

```bash
python3 your_script_name.py
```

Ensure that **"Orders.xlsx"** is in the same directory before running the script.

## Notes

- Adjust any column names or filtering criteria in the code as necessary to fit your data structure.
- The script includes various formatting options for the output file to enhance readability.
```

Feel free to customize any sections as needed!
