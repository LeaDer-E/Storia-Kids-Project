from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
from config import *
import time
import os
import re

# Initialize the WebDriver with options
#driver = uc.Chrome(version_main=127)
driver = uc.Chrome(version_main=128)
# Open the login page
driver.get('https://stage.storiagate.com/****')

# Find the username and password fields and enter the credentials
username_field = driver.find_element(By.NAME, 'username')  # Update 'username' to the actual name attribute of the username input field
password_field = driver.find_element(By.NAME, 'password')  # Update 'password' to the actual name attribute of the password input field

# Enter the login credentials
username_field.send_keys('****')  # Replace with your actual username
password_field.send_keys('****')  # Replace with your actual password

# Submit the login form
password_field.send_keys(Keys.RETURN)

# After login, navigate to the desired page
driver.get('https://stage.storiagate.com/****')


    
################################################################################################################
######################################## Send To Delivery Whatsapp Group #######################################
################################################################################################################

def S_T_D(STD):
    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()
        
        # Locate the input field and enter the value of Cst_No_Answer
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        input_field.send_keys(STD)  # Write Order Here

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Define the old Status for the Order
        old_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[10]'))
        )

        # Define the order Pakcage
        package = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr[1]/td[7]'))
        )
        
        if old_status.text in ["Sent to Delivery", "Delivered"]:
            print(f'Order No. : {STD}')
            print(f'Old Status: >> {old_status.text}  there\'s nothing to change here<<')
            print("")
            print('=====================================')
            print("")
            return  # Exit the function to skip further processing for this order
            
            
        print(f'Order No. : {STD}')
        print(f'Old Status: >> {old_status.text} <<')
        print("")
        print('=====================================')
        print("")
       
        # Change the Value Status
        Edit_Status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[12]/div/a[1]/i'))
        )
        Edit_Status.click()

        # Define the regular expression pattern
        pattern = r"D:\d+"

        # Check if package_text matches the pattern
        if re.match(pattern, package.text):
            # Select "Send To Delivery"
            Send_To_Delivery = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[7]'))
            )
            Send_To_Delivery.click()
        else:
            # Select "Send To Delivery"
            Send_To_Delivery = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[8]'))
            )
            Send_To_Delivery.click()

        # Submit
        Submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="order-status-popup"]/div/div[2]/div/form/div[8]/button'))
        )
        Submit.click()

        # Handle the alert
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No alert found.")
            
    except ElementNotInteractableException as e:
        print(f"{STD} >> Error ######################################")
        print(f"Error: Element not interactable - {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")

    except Exception as e:
        print(f"{STD} >> Error ######################################")
        print("")
        print('=====================================')
        print("")



def STD():
    print("")
    print('=====================================')
    print("")
    # Loop through each number in the array and call S_T_D()
    for STD in STD_List:
        S_T_D(STD)
    print('###########################################################')
    print('## All Orders Changed to Send To Delivery Whatsapp Group ##')
    print('###########################################################')


    
################################################################################################################
######################################### Pending Customer Confirmation ########################################
################################################################################################################

def P_C_C(PCC):
    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()

        # Locate the input field and enter the value of PCC
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        input_field.send_keys(PCC)
        
        Order_ID_in_Array = PCC

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Define the old Status for the Order
        old_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[10]'))
        )
        
        if old_status.text in ["Pending Edit", "Pending Customer Confirmation", "Sent to Delivery", "Delivered"]:
            print(f'Order No. : {Order_ID_in_Array}')
            print(f'Old Status: >> {old_status.text}  there\'s nothing to change here<<')
            print("")
            print('=====================================')
            print("")
            return  # Exit the function to skip further processing for this order
            
        print(f'Order No. : {PCC}')
        print(f'Old Status: >> {old_status.text} <<')
        print("")
        print('=====================================')
        print("")

        # Change the Value Status
        Edit_Status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[12]/div/a[1]/i'))
        )
        Edit_Status.click()

        # Select "Pending Customer Confirmation"
        Pending_C_C = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[2]'))
        )
        Pending_C_C.click()

        # Submit
        Submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="order-status-popup"]/div/div[2]/div/form/div[8]/button'))
        )
        Submit.click()

        # Handle the alert
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No alert found.")

    except ElementNotInteractableException as e:
        print(f"{PCC} >> >> Error ######################################")
        print(f"Error: Element not interactable - {e}")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")

    except Exception as e:
        print(f"{PCC} >> >> Error ######################################")
        print(f"error is {e}")
        print('=====================================')
        print("")

def PCC():
    print("")
    print('=====================================')
    print("")
    # Loop through each number in the array and call P_C_C()
    for PCC in PCC_List:
        P_C_C(PCC)
    print('#########################################################')
    print('## All Orders Changed to Pending Customer Confirmation ##')
    print('#########################################################')
    


################################################################################################################
######################################## SPending Another Story #######################################
################################################################################################################

def P_A_S(PAS):
    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()

        # Locate the input field and enter the value of Cst_No_Answer
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        input_field.send_keys(PAS)  # Write Order Here

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Define the old Status for the Order
        old_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[10]'))
        )

        if old_status.text in ["Pending Edit", "Pending Another Story", "Sent to Delivery", "Delivered"]:
            print(f'Order No. : {PAS}')
            print(f'Old Status: >> {old_status.text}  there\'s nothing to change here<<')
            print("")
            print('=====================================')
            print("")
            return  # Exit the function to skip further processing for this order

        
        print(f'Order No. : {PAS}')
        print(f'Old Status: >> {old_status.text} <<')
        print("")
        print('=====================================')
        print("")

        # Change the Value Status
        Edit_Status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[12]/div/a[1]/i'))
        )
        Edit_Status.click()

        # Select "Send To Delivery"
        Send_To_Delivery = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[6]'))
        )
        Send_To_Delivery.click()

        # Submit
        Submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="order-status-popup"]/div/div[2]/div/form/div[8]/button'))
        )
        Submit.click()

        # Handle the alert
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No alert found.")

    except ElementNotInteractableException as e:
        print(f"{PAS} >> Error ######################################")
        print(f"Error: Element not interactable - {e}")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")

    except Exception as e:
        print(f"{PAS} >> Error ######################################")
        print("")
        print('=====================================')
        print("")



def PAS():
    print("")
    print('=====================================')
    print("")
    # Loop through each number in the array and call S_T_D()
    for PAS in PAS_List:
        P_A_S(PAS)
    print('#################################################')
    print('## All Orders Changed to Pending Another Story ##')
    print('#################################################')

################################################################################################################
############################################## Customer No Response ############################################
################################################################################################################


def No_Res(Cst_No_Answer):
    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()

        # Locate the input field and enter the value of Cst_No_Answer
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        input_field.send_keys(Cst_No_Answer)

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Define the old Status for the Order
        old_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[10]'))
        )
        
        if old_status.text in ["Pending Edit", "No Response", "Sent to Delivery", "Delivered"]:
            print(f'Order No. : {Cst_No_Answer}')
            print(f'Old Status: >> {old_status.text}  there\'s nothing to change here<<')
            print("")
            print('=====================================')
            print("")
            return  # Exit the function to skip further processing for this order
            
            
        print(f'Order No. : {Cst_No_Answer}')
        print(f'Old Status: >> {old_status.text} <<')
        print("")
        print('=====================================')
        print("")

        # Change the Value Status
        Edit_Status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[12]/div/a[1]/i'))
        )
        Edit_Status.click()

        # Select "No Response"
        NO_Response = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[4]'))
        )
        NO_Response.click()

        # Submit
        Submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="order-status-popup"]/div/div[2]/div/form/div[8]/button'))
        )
        Submit.click()

        # Handle the alert
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()
        except NoAlertPresentException:
            print("No alert found.")

    except ElementNotInteractableException as e:
        print(f"{Cst_No_Answer} >> >> Error ######################################")
        print(f"Error: Element not interactable - {e}")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except Exception as e:
        print(f"{Cst_No_Answer} >> >> Error ######################################")
        print("")
        print('=====================================')
        print("")

def No_Response():
    print("")
    print('=====================================')
    print("")
    # Loop through each number in the array and call No_Res()
    for Cst_No_Answer in Cst_No_Answer_List:
        No_Res(Cst_No_Answer)
    print('######################################')
    print('## All Orders Changed To No Response ##')
    print('######################################')





    
################################################################################################################
############################################## Download Story ############################################
################################################################################################################
def Edits_DW(DW):
    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()

        # Locate the input field and enter the value of DW
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        input_field.send_keys(DW)

        # Confirm Filter
        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Select the Order
        Select_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[1]/div/input'))
        )
        Select_Order.click()

        # Download The Order
        Download_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[1]/button'))
        )
        Download_Order.click()

        print(f"Order {DW} downloaded successfully.")
        print("")
        print('=====================================')
        print("")

    except ElementNotInteractableException as e:
        print(f"Error with Order {DW}: Download Faild")
        print(f"Error: Element not interactable - {e}")

    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")

    except Exception as e:
        print(f"Error with Order {DW}: Download Faild")
        print("")
        print('=====================================')
        print("")

def Download():
    print("")
    print('=====================================')
    print("")
    # Loop through each order in the list and call Edits_DW()
    for DW in DW_List:
        Edits_DW(DW)
    print('#############################################')
    print('## All Orders have Downloaded Successfully ##')
    print('#############################################')


################################################################################################################
############################################## Download Story ############################################
################################################################################################################

# Error counters
error_count = 0

def Edits_DW1(DW):
    global error_count  # Ensure the function uses the global error_count

    try:
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

        # Select Delivery View
        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        # Select Filter
        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()

        # Locate the input field and enter the value of DW
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()  # Clear any existing text
        time.sleep(0.5)
        input_field.send_keys(DW)

        # Confirm Filter
        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()

        # Select the Order
        Select_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[1]/div/input'))
        )
        Select_Order.click()

        # Download The Order
        Download_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[1]/button'))
        )
        Download_Order.click()
        
        # Function to handle alerts and count errors
        def check_alerts():
            global error_count  # Ensure we are modifying the global variable
            try:
                # Wait for an alert to be present
                alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert.accept()  # Accept the alert
                error_count += 1  # Increment the error counter
            except NoAlertPresentException:
                pass  # No alert present, do nothing
            except TimeoutException:
                pass  # Timeout waiting for alert, do nothing

        # Check for up to two alerts
        for _ in range(2):
            check_alerts()

        # Print messages based on the number of errors
        if error_count == 0:
            print(f"Order {DW} downloaded successfully.")
            print("")
            print('=====================================')
            print("")
        elif error_count in [1, 2]:
            print(f"Order {DW} Download Failed")
            print(f"We have {error_count} Alert{'s' if error_count > 1 else ''}.")
            print("")
            print('=====================================')
            driver.back()
        else:
            print(f"Unexpected number of Alerts: {error_count}.")
            print("")
            print('=====================================')
            driver.back()

    except ElementNotInteractableException as e:
        print(f"Error with Order {DW}: Download Failed")
        print(f"Error: Element not interactable - {e}")
    except NoSuchElementException as e:
        print(f"Error: Element not found - {e}")
    except Exception as e:
        print(f"Error with Order {DW}: Download Failed")
        print("")
        print('=====================================')
    
    # Reset error_count after the function ends
    error_count = 0
    

def Downloads():
    print("")
    print('=====================================')
    print("")
    # Loop through each order in the list and call Edits_DW()
    for DW in DW_List:
        Edits_DW1(DW)
    print('#############################################')
    print('## All Orders have Downloaded Successfully ##')
    print('#############################################')



PCC()

#No_Response()

#PAS()

#STD()

#Downloads()

