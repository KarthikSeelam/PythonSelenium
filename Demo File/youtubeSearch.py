from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

search_bar = driver.find_element(By.XPATH, "//*[@class='gLFyf']")
search_bar.send_keys("Youtube")
time.sleep(3)
search_bar.send_keys(Keys.ENTER)
time.sleep(5)
youtube_link = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a")
youtube_link.click()
time.sleep(10)
youtube_search = driver.find_element(By.XPATH, "//*[@name='search_query']")
youtube_search.send_keys("Python Selenium")
yt_search_btn = driver.find_element(By.XPATH, "//*[@id='search-icon-legacy']")
yt_search_btn.click()
time.sleep(10)