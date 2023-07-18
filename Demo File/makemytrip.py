from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

print("sample test started")
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.makemytrip.com/")
actions = ActionChains(driver)

# Find the body element
body_element = driver.find_element(By.TAG_NAME, "body")
# Perform a click action on the body element
# driver.find_element()


time.sleep(1000)
try:

    driver.find_element(By.XPATH, "//*[@id='webklipper-publisher-widget-container-notification-close-div']").click()
    driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[1]/ul/li[4]").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("123456789")
    actions.move_to_element(body_element).click().perform()



except:
    driver.find_element(By.XPATH, "//*[@id='SW']/div[1]/div[1]/ul/li[4]").click()
    time.sleep(10)

    driver.find_element(By.XPATH, "//*[@id='username']").send_keys("123456789")
    actions.move_to_element(body_element).click().perform()


driver.close()
print("sample test successfully completed")
