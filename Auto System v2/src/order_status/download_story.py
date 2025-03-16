import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from src.config import DW_List

error_count = 0

def Edits_DW1(driver, DW):
    global error_count
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
        time.sleep(1)
        input_field.send_keys(DW)

        Filter_Confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/section[2]/section/div[6]/button'))
        )
        Filter_Confirm.click()
        time.sleep(1)
        
        Select_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="download-form"]/table/tbody/tr/td[1]/div/input'))
        )
        Select_Order.click()
        time.sleep(1)
        
        Download_Order = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section[2]/section[1]/form/div[1]/button'))
        )
        Download_Order.click()
        
        def check_alerts():
            global error_count
            try:
                alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert.accept()
                error_count += 1
            except NoAlertPresentException:
                pass
            except TimeoutException:
                pass

        for _ in range(2):
            check_alerts()

        if error_count == 0:
            print(f"Order {DW} downloaded successfully.\n=====================================\n")
        elif error_count in [1, 2]:
            print(f"Order {DW} Download Failed")
            print(f"We have {error_count} Alert{'s' if error_count > 1 else ''}.\n=====================================\n")
            driver.back()
        else:
            print(f"Unexpected number of Alerts: {error_count}.\n=====================================\n")
            driver.back()

    except ElementNotInteractableException as e:
        print(f"Error with Order {DW}: Download Failed")
        print(f"Error: Element not interactable - {e}")
    except ElementNotInteractableException as e:
        print(f"Error: Element not found - {e}")
        return None
    except Exception as e:
        print(f"Error with Order {DW}: Download Failed\n=====================================\n")
    
    error_count = 0

    
def Downloads(driver):
    print("\n=====================================\n")
    # Update DW.txt from DWList.txt
    from src.file_processing import process_numbers
    process_numbers("DWLIST.txt", "DW.txt")
    # Reload DW_List After Update
    from src.config import read_file_to_list
    global DW_List
    DW_List = read_file_to_list("DW.txt")
    # Verify New Numbers After Edit
    print("Updated DW_List:", DW_List)
    print('#############################################')
    for DW_val in DW_List:
        Edits_DW1(driver, DW_val)

    print('#############################################')
    print('## All Orders have Downloaded Successfully ##')
    print('#############################################')

