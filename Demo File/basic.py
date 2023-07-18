from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://in.bookmyshow.com/explore/home/hyderabad"
driver.get(url)
time.sleep(3)
moviesList1 = driver.find_elements(By.CSS_SELECTOR, ".sc-lnhrs7-4.bmyqGC a")

for link_element in moviesList1:
    # Extract the URL from the link element
    url = link_element.get_attribute("href")

    # Open the URL in a new tab
    driver.execute_script(f"window.open('{url}')")
    time.sleep(10)
# Switch to each tab and perform actions (e.g., print the page title)
for i, handle in enumerate(driver.window_handles):
    driver.switch_to.window(handle)
    print(f"Tab {i + 1} - Title: {driver.title}")

    # You can perform additional actions on each tab here
time.sleep(5)
# Close the browser
driver.quit()