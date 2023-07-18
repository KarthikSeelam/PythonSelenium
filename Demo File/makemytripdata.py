import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


url = 'https://www.makemytrip.com/'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

try:
    close_button = driver.find_element(By.XPATH,
                                       "//*[@id='webklipper-publisher-widget-container-notification-close-div']")
    close_button.click()
except NoSuchElementException:
    pass

action = ActionChains(driver)
action.move_by_offset(100, 100).click().perform()

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/p/a").click()
time.sleep(5)

data_list = []

try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/button").click()
except NoSuchElementException:
    pass
print("Before Slides XPATH")
slides = driver.find_elements(By.XPATH, "//div[contains(@class, 'weeklyFareItems')]")

num_slides = len(slides)
print("After Slides XPATH")
print(num_slides, " Number of Slides")

for slide in slides:
    try:
        # Extract flight details from the current slide
        data = slide.find_elements(By.XPATH, ".//div[@class='fli-list']")

        for details in data:
            # Extract flight details from the current slide
            flightName = details.find_element(By.XPATH, ".//p[contains(@class, 'boldFont blackText airlineName')]").text
            fromTime = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoLeft')]//span").text
            fromPlace = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoLeft')]/p[2]").text
            toTime = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoRight')]//span").text
            toPlace = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoRight')]/p[2]").text
            price = details.find_element(By.XPATH,
                                         ".//div[contains(@class, 'blackText fontSize18 blackFont white-space-no-wrap')]").text

            data_items = {
                'Flight Name': flightName,
                'Departure Time': fromTime,
                'Source Location': fromPlace,
                'Arrival Time': toTime,
                'Destination': toPlace,
                'Ticket Price': price
            }
            data_list.append(data_items)

    except StaleElementReferenceException:
        # If the element becomes stale, re-find the slide element
        slides = driver.find_elements(By.XPATH, "//div[contains(@class, 'weeklyFareItems')]")

        # Re-find the slide element using a unique identifier, such as flightName
        slide_element = None
        for s in slides:
            try:
                flight_name = s.find_element(By.XPATH, ".//p[contains(@class, 'boldFont blackText airlineName')]").text
                if flight_name == flightName:
                    slide_element = s
                    break
            except NoSuchElementException:
                continue

        if slide_element is not None:
            slide = slide_element
            data = slide.find_elements(By.XPATH, ".//div[@class='fli-list']")

            for details in data:
                # Extract flight details from the refreshed slide
                flightName = details.find_element(By.XPATH,
                                                  ".//p[contains(@class, 'boldFont blackText airlineName')]").text
                fromTime = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoLeft')]//span").text
                fromPlace = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoLeft')]/p[2]").text
                toTime = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoRight')]//span").text
                toPlace = details.find_element(By.XPATH, ".//div[contains(@class, 'timeInfoRight')]/p[2]").text
                price = details.find_element(By.XPATH,
                                             ".//div[contains(@class, 'blackText fontSize18 blackFont white-space-no-wrap')]").text

                data_items = {
                    'Flight Name': flightName,
                    'Departure Time': fromTime,
                    'Source Location': fromPlace,
                    'Arrival Time': toTime,
                    'Destination': toPlace,
                    'Ticket Price': price
                }
                data_list.append(data_items)

    # Click on the next slide
    slide.click()
    time.sleep(5)

df = pd.DataFrame(data_list)
print(df)
