import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.chrome.options import Options

# CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# CHROMEDRIVER_PATH = 'C:\Program Files (x86)\chromedriver.exe'
# WINDOW_SIZE = "1920,1080"

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH

# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options, service=Service(ChromeDriverManager().install()))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.ubereats.com/ca")

search_input = driver.find_element(By.ID, "location-typeahead-home-input")
search_input.send_keys("555 Seymour St")

time.sleep(5)
search_input.send_keys(Keys.RETURN)

time.sleep(5)

try:
    restaurant_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "searchTerm"))
    )
    time.sleep(5)
    restaurant_search.send_keys("mcdonalds")
    time.sleep(5)
    restaurant_search.send_keys(Keys.RETURN)
except:
    driver.quit()

time.sleep(5)

try:
    granville = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.LINK_TEXT, "McDonald's (Granville)")
    )
    time.sleep(5)
    granville.click()
    time.sleep(5)
except:
    driver.quit()
driver.quit()