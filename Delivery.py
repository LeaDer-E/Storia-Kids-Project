from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
from tabulate import tabulate
from config import *
import time
import os
import re

# Define the dark mode CSS styles
dark_mode_css = """
document.body.style.backgroundColor = '#121212'; /* Dark background */
document.body.style.color = '#ffffff';           /* Light text */

let elements = document.querySelectorAll('*');
for (let element of elements) {
    element.style.backgroundColor = '#121212';
    element.style.color = '#ffffff';
    element.style.borderColor = '#444444';      /* Optional: Darker borders */
}
"""



# Initialize the WebDriver with options
driver = uc.Chrome(version_main=128)

# Open the login page
driver.get('https://stage.storiagate.com/****.****')

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.NAME, 'username')  # Update 'username' to the actual name attribute of the username input field
password_field = driver.find_element(By.NAME, 'password')  # Update 'password' to the actual name attribute of the password input field

# Enter the login credentials
username_field.send_keys('**********')  # Replace with your actual username
password_field.send_keys('**********')  # Replace with your actual password

# Submit the login form
password_field.send_keys(Keys.RETURN)

# After login, navigate to the desired page
driver.get('https://stage.storiagate.com/dhome.php')


def reverse_text(text):
    """Reverse the given text."""
    return text[::-1]

def is_arabic(text):
    """Check if the text contains Arabic characters."""
    return bool(re.search(r'[\u0600-\u06FF]', text))

def Delivery():
    while True:
        start_time = time.time()
        try:
            user_input = input("Please enter the Order ID (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            # Define XPath for the element to remove
            element_xpath = '/html/body/div[2]'
            
            # Check if the element exists and remove it if found
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, element_xpath))
                )
                driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element)
            except NoSuchElementException:
                pass

            # Step 1: Select Orders View
            orders_view = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Orders"))
            )
            orders_view.click()

            # Step 2: Click the Filter Button
            filter_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div/button'))
            )
            filter_button.click()

            # Step 3: Enter the Order ID into the input field
            input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section/section/div[1]/input'))
            )
            input_field.clear()  # Clear any existing text
            input_field.send_keys(user_input)  # Input the user's text

            # Step 4: Click the Filter Confirmation Button
            filter_conf_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section/section/div[5]/button'))
            )
            filter_conf_button.click()
            

            # Step 5: Copy the text from the specified element
            try:
                chat_ref_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//td[@data-cell="Chat Ref"]'))
                )
                copied_text = chat_ref_element.text  # Copy the text
            except TimeoutException:
                print("Chat Ref element not found.")
                continue

            # Step 6: Click the Filter Button Again
            filter_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div/button'))
            )
            filter_button.click()

            # Step 7: Enter the copied text into another input field
            new_input_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section/section/div[3]/input'))
            )
            new_input_field.clear()  # Clear any existing text
            new_input_field.send_keys(copied_text)  # Paste the copied text

            # Step 8: Click the Filter Confirmation Button Again
            filter_conf_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section/section/div[5]/button'))
            )
            filter_conf_button.click()
            
            order_ids = []  # Initialize for Order_IDs
            rows = []  # Initialize for rows
            orders_data = []  # Initialize for orders_data
            Deposit = 0.0  # Initialize total for Deposit
            Discount = 0.0  # Initialize total for Discount
            TotalPrice = 0.0  # Initialize total for TotalPrice
            GrandTotal = 0.0  # Initialize total for GrandTotal
            total_lefttopay = 0.0  # Initialize total for lefttopay
            print("Please wait, processing orders...")
            driver.execute_script(dark_mode_css)

            for i in range(1, 31):  # Check for 30 orders
                try:
                    # Construct the XPaths for ID and Status
                    id_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[1]'
                    childname_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[5]'
                    PaymentStatues_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[8]'
                    country_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[9]'
                    Deposit_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[10]'
                    Discount_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[11]'
                    TotalPrice_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[12]'
                    GrandTotal_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[13]'
                    confirmation_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[15]'
                    lefttopay_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[14]'
                    status_xpath = f'//*[@id="app"]/section[2]/div[2]/table/tbody/tr[{i}]/td[18]'

                    # Explicit wait to ensure elements are present
                    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, status_xpath)))
                    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, childname_xpath)))
                    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lefttopay_xpath)))
                    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, country_xpath)))

                    # Find the elements
                    id_element = driver.find_element(By.XPATH, id_xpath)
                    childname_element = driver.find_element(By.XPATH, childname_xpath)
                    paymentstatues_element = driver.find_element(By.XPATH, PaymentStatues_xpath)
                    country_element = driver.find_element(By.XPATH, country_xpath)
                    deposit_element = driver.find_element(By.XPATH, Deposit_xpath)
                    discount_element = driver.find_element(By.XPATH, Discount_xpath)
                    totalprice_element = driver.find_element(By.XPATH, TotalPrice_xpath)
                    grandtotal_element = driver.find_element(By.XPATH, GrandTotal_xpath)
                    confermation_element = driver.find_element(By.XPATH, confirmation_xpath)
                    lefttopay_element = driver.find_element(By.XPATH, lefttopay_xpath)
                    status_element = driver.find_element(By.XPATH, status_xpath)  

                    # Get the text
                    id_text = id_element.text
                    status_text = status_element.text
                    childname_text = childname_element.text
                    country_text = country_element.text
                    confermation_text = confermation_element.text
                    paymentstatus_text = paymentstatues_element.text


                    if confermation_text == "Confirmed":
                        # Reverse the child name if it contains Arabic characters
                        if is_arabic(childname_text):
                            childname_text = reverse_text(childname_text)

                        # Extract and convert lefttopay text to float
                        lefttopay_text = lefttopay_element.text.replace(',', '')  # Remove commas if present
                        # Check if the text is not empty
                        if lefttopay_text.strip():  # strip() removes any surrounding whitespace
                            lefttopay_no = float(lefttopay_text)
                        else:
                            lefttopay_no = 0.0
                            
                        total_lefttopay += lefttopay_no  # Add to total


                        # Extract and convert Deposit text to float
                        deposit_text = deposit_element.text.replace(',', '')  # Remove commas if present
                        # Check if the text is not empty
                        if deposit_text.strip():
                            deposit_no = float(deposit_text)
                        else:
                            deposit_no = 0.0
                            
                        Deposit += deposit_no  # Add to total

                        # Extract and convert Discount text to float
                        discount_text = discount_element.text.replace(',', '')  # Remove commas if present
                        # Check if the text is not empty
                        if discount_no.strip():
                            discount_no = float(discount_text)
                        else:
                            discount_no = 0.0
                            
                        Discount += discount_no  # Add to total

                        # Extract and convert TotalPrice text to float
                        totalprice_text = totalprice_element.text.replace(',', '')  # Remove commas if present
                        totalprice_no = float(totalprice_text)
                        TotalPrice += totalprice_no  # Add to total


                        # Extract and convert GrandTotal text to float
                        grandtotal_text = grandtotal_element.text.replace(',', '')  # Remove commas if present
                        # Check if the text is not empty
                        if grandtotal_text.strip():  # strip() removes any surrounding whitespace
                            grandtotal_no = float(grandtotal_text)  # Convert to float
                        else:
                            grandtotal_no = 0.0  # Default value if text is empty
                            
                        GrandTotal += grandtotal_no  # Add to total

                        # Add ID to the list
                        order_ids.append(int(id_text))  # Convert to integer for sorting
                        rows.append([id_text, childname_text, paymentstatus_text, status_text])

                        # Print the results
                        #print(f'{id_text} >> {childname_text} > {paymentstatus_text} > {status_text}')
                        line = f'{id_text} >> {childname_text} > {paymentstatus_text} > {status_text}'
                        orders_data.append(line)


                except NoSuchElementException:
                # Sort and print the order IDs
                    print(f"Error with Order {user_input}")
                    continue

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print("\n" + "="*50 + "\n")
            print(f'-----------------Order No.: {user_input}-----------------')
            print("\n" + "="*50 + "\n")
            output = tabulate(rows, headers=['Order ID', 'Child Name', 'Payment Status', 'Status'], tablefmt='heavy_grid')
            print(f'{output}')
            print("\n" + "="*50 + "\n")
            print(f'-----------------Order No.: {user_input}-----------------')
            print("\n" + "="*50 + "\n")
            for index, line in enumerate(orders_data, start=1):
                print("\n" + "-"*50 + "\n")
                print(f'{index} | {line}')
            print("\n" + "="*50 + "\n")
            order_ids_sorted = sorted(order_ids)
            print("Orders ID:", ", ".join(f"#{id}" for id in order_ids_sorted))
            print('\n')
            print(f'Total Deposit: {Deposit:.2f} {country_text}')
            print(f'Total Discount: {Discount:.2f} {country_text}')
            print(f'Total Total Price: {TotalPrice:.2f} {country_text}')
            print(f'Total Grand Total: {GrandTotal:.2f} {country_text}')
            print(f'Total Left To Pay: {total_lefttopay:.2f} {country_text}')
            print("\n" + "="*50 + "\n")
            end_time = time.time()
            duration = end_time - start_time
            print(f"Total time taken: {duration:.2f} seconds")
            print("\n\n")    
                
           

        except Exception as e:
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print("\n" + "="*50 + "\n")
            print(f'-----------------Order No.: {user_input}-----------------')
            print("\n" + "="*50 + "\n")
            output = tabulate(rows, headers=['Order ID', 'Child Name', 'Payment Status', 'Status'], tablefmt='heavy_grid')
            print(f'{output}')
            print("\n" + "="*50 + "\n")
            print(f'-----------------Order No.: {user_input}-----------------')
            print("\n" + "="*50 + "\n")
            for index, line in enumerate(orders_data, start=1):
                print("\n" + "-"*50 + "\n")
                print(f'{index} | {line}')
            print("\n" + "="*50 + "\n")
            order_ids_sorted = sorted(order_ids)
            print("Orders ID:", ", ".join(f"#{id}" for id in order_ids_sorted))
            print('\n')
            print(f'Total Deposit: {Deposit:.2f} {country_text}')
            print(f'Total Discount: {Discount:.2f} {country_text}')
            print(f'Total Total Price: {TotalPrice:.2f} {country_text}')
            print(f'Total Grand Total: {GrandTotal:.2f} {country_text}')
            print(f'Total Left To Pay: {total_lefttopay:.2f} {country_text}')
            print("\n" + "="*50 + "\n")
            end_time = time.time()
            duration = end_time - start_time
            print(f"Total time taken: {duration:.2f} seconds")
            print("\n\n")


Delivery()

