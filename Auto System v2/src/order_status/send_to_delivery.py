import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import STD_List

def S_T_D(driver, STD):
    try:
        element_xpath = '/html/body/div[2]'
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )
            driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element)
        except NoSuchElementException:
            pass

        Delivery_View = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/aside/div[2]/ul/li[5]/a/span[1]'))
        )
        Delivery_View.click()

        Filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[2]/button/i'))
        )
        Filter.click()
        
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[1]/input'))
        )
        input_field.clear()
        input_field.send_keys(STD)

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()
        time.sleep(1)
        
        old_status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[10]'))
        )
        package = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="download-form"]/table/tbody/tr[1]/td[7]'))
        )
        
        if old_status.text in ["Sent to Delivery", "Delivered"]:
            print(f'Order No. : {STD}')
            print(f'Old Status: >> {old_status.text}  there\'s nothing to change here<<')
            print("\n=====================================\n")
            return
        
        print(f'Order No. : {STD}')
        print(f'Old Status: >> {old_status.text} <<')
        print("\n=====================================\n")
       
        Edit_Status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[12]/div/a[1]/i'))
        )
        Edit_Status.click()

        import re
        pattern = r"D:\d+"
        if re.match(pattern, package.text):
            Send_To_Delivery = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[7]'))
            )
            Send_To_Delivery.click()
        else:
            Send_To_Delivery = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="inStatus"]/option[8]'))
            )
            Send_To_Delivery.click()

        Submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="order-status-popup"]/div/div[2]/div/form/div[8]/button'))
        )
        Submit.click()

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
        print("\n=====================================\n")

def STD(driver):
    print("\n=====================================\n")
    for STD_val in STD_List:
        S_T_D(driver, STD_val)
    print('###########################################################')
    print('## All Orders Changed to Send To Delivery Whatsapp Group ##')
    print('###########################################################')
