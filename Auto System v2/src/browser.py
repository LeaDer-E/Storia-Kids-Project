import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def open_browser_without_ads():
    """Set up the browser without ads and return the WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--lang=en")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-gpu")
    
    driver = uc.Chrome(options=options, version_main=134)
    return driver

def login(driver):
    """Perform login to the website using the provided driver."""
    driver.get('https://stage.storiagate.com/login.php')
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')
    username_field.send_keys('Eslam.Mustafa')
    password_field.send_keys('56259595625959')
    password_field.send_keys(Keys.RETURN)
    time.sleep(2)