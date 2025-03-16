# Orders Automation Project

This project automates order processing tasks using Selenium with Undetected ChromeDriver.

## Project Structure

```plaintext
project_root/
├── main.py
├── PCC.txt             (Put Orders Here)
├── PAS.txt             (Put Orders Here)
├── NoRes.txt           (Put Orders Here)
├── DW.txt              (don't Change any thing here it will changed Automaticly from DWLIST.txt)
├── STD.txt             (Put Orders Here)
├── DWLIST.txt          (Put Orders Here with any other things, it will take Orders ID only)
├── requirements.txt
├── README.md
└── src/
    ├── browser.py
    ├── config.py
    ├── file_processing.py
    └── order_status/
          ├── __init__.py
          ├── send_to_delivery.py
          ├── pending_customer_confirmation.py
          ├── pending_another_story.py
          ├── customer_no_response.py
          └── download_story.py
```
- **main.py**: Main entry point for the application.
- **PCC.txt, PAS.txt, NoRes.txt, DW.txt, STD.txt, DWLIST.txt**: Empty text files for storing order IDs or other data (populate as needed).
- **src/**: Contains the project's Python modules:
  - **browser.py**: Browser initialization and login functions.
  - **config.py**: Loads order lists from text files.
  - **file_processing.py**: Helper function to process number files.
  - **order_status/**: Modules for each group of order status functions:
      - **send_to_delivery.py**: Functions for "Send To Delivery Whatsapp Group".
      - **pending_customer_confirmation.py**: Functions for "Pending Customer Confirmation".
      - **pending_another_story.py**: Functions for "Pending Another Story".
      - **customer_no_response.py**: Functions for "Customer No Response".
      - **download_story.py**: Functions for "Download Story".
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Project documentation.

## Setup

1. Clone the repository.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Populate the empty text files (PCC.txt, PAS.txt, NoRes.txt, DW.txt, STD.txt, DWLIST.txt) with the appropriate data as needed.

## Running the Application
# Run the main application with:
   ```bash
   python main.py
   ```

## License
MIT License. EOF
