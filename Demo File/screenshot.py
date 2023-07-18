from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://selenium-python.readthedocs.io/faq.html#how-to-take-screenshot-of-the-current-window")
driver.save_screenshot("screenshot1.png")
driver.quit()