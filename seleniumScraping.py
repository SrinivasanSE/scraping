# https://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service = Service("E:/chromedriver.exe"),options=webdriver.ChromeOptions())
# driver.get("https://finance.yahoo.com/")
# print(driver.current_url)

# # Filling and submit
# search_element = driver.find_element(By.ID,"yfin-usr-qry")
# search_element.clear()
# search_element.send_keys("TSLA")
# #search_element.send_keys(Keys.RETURN)
# driver.find_element(By.ID,"header-desktop-search-button").click()

# The quit will exit entire browser whereas close will close one tab, but if just one tab was open, by default most browser will exit entirely
#driver.close()
#driver.quit()

# Selecting from dropdown
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
# select_element = driver.find_element(By.CLASS_NAME, "nav-search-dropdown")
# select = Select(select_element)
# select.select_by_index(6)
# select.select_by_visible_text("Electronics")
# select.select_by_value("search-alias=computers")
# print(select.first_selected_option.text)
# for option in select.options:
#     print(option.text, option.get_attribute('value')) 
# input_field = driver.find_element(By.NAME, "field-keywords")
# input_field.send_keys("dell")
# input_field.send_keys(Keys.RETURN)
# print(select.all_selected_options)
#print(select.deselect_all())
# driver.minimize_window()

# Navigation

# driver.execute_script("window.open();")
# driver.execute_script("window.open();")
# print(driver.window_handles)
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
# driver.back()
# driver.forward()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nav-search-dropdown"))
    )
    driver.save_screenshot('amazon.png')
    driver.get_screenshot_as_file('amazon.png')
    print(element.text)
finally:
    driver.quit()