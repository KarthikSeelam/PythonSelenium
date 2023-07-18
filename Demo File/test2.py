from telnetlib import EC
from turtle import title

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

print("Sample Test Started")

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to YouTube
driver.get("https://www.youtube.com/")
time.sleep(3)

# Enter search query
search_box = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_box.send_keys("24K Magic")

# Click on the search button
search_button = driver.find_element(By.CSS_SELECTOR, '#search-icon-legacy.ytd-searchbox')
search_button.click()
video_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-video-renderer #video-title")))
video_link.click()
wait = WebDriverWait(driver, 20*60)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='skip-button:6']/span/button")))


time.sleep(1000)
# Rest of the code...

