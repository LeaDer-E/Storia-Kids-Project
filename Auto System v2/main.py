  GNU nano 7.2                                                                                main.py                                                                                         
import time
from src.browser import open_browser_without_ads, login
from src.order_status.send_to_delivery import STD
from src.order_status.pending_customer_confirmation import PCC
from src.order_status.pending_another_story import PAS
from src.order_status.customer_no_response import No_Response
from src.order_status.download_story import Downloads
from src.file_processing import process_numbers

if __name__ == "__main__":
    # Optionally process numbers from DWLIST.txt (if needed)
    #process_numbers("DWLIST.txt", "DW.txt")

    driver = open_browser_without_ads()
    login(driver)
    driver.get('https://stage.storiagate.com/dhome.php')

    ## Uncomment the functions you want to run:
    # PCC(driver)
    # No_Response(driver)
    # PAS(driver)
    # STD(driver)
    # Downloads(driver)

    time.sleep(2)
    driver.quit()
