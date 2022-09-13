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

# typing in BCIT address and pressing enter
search_input = driver.find_element(By.ID, "location-typeahead-home-input")
search_input.send_keys("555 Seymour St")
time.sleep(5)
search_input.send_keys(Keys.RETURN)
time.sleep(5)

# waits until search bar is visible in DOM and enters mcdonalds
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

# waits until mcdonalds granville listing is visible and clicks it
try:
    granville = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div[3]/div/section/div[2]/div[1]/li[1]/div/a/h3'))
    )
    time.sleep(5)
    granville.click()
    print('clicked granville mcdonalds')
    time.sleep(5)
except:
    driver.quit()

# waits until 'individual items' button is loaded and clicks it
try:
    individual_items_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[4]/div[4]/div[2]/div[1]/div[2]/div/div/nav/div[12]/button/div'))
    )
    time.sleep(5)
    individual_items_button.click()
    print('clicked individual items')
    time.sleep(5)
except:
    driver.quit()


item_data = []
try:
    item_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[4]/div[4]/div[4]/ul/li[12]/ul/li[10]/div/div/div[2]/div[1]/div/span'))
    )
    item_data.append(item_name.text)
    print('read item name')
except:
    driver.quit()
time.sleep(3)
try:
    item_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[4]/div[4]/div[4]/ul/li[12]/ul/li[10]/div/div/div[2]/div[2]/span'))
    )
    item_data.append(item_price.text)
    print('read item price')
except:
    driver.quit()

for i in item_data:
    print(i)
driver.quit()