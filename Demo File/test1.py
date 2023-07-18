from selenium.webdriver.common.by import By
from selenium import webdriver
import time

print("sample test started")
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://contractbook.com/")

# driver.find_element()

driver.find_element(By.XPATH, "/html/body/div/div/div[1]/nav/div[2]/div/div[1]/div[2]/div[1]/a").click()
time.sleep(3)

try:

    driver.find_element(By.XPATH, "//*[@id='lm-cookie-wall-container']/div/div[1]/*[name()='svg']").click()


    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div[2]/div/form/div/div/input").send_keys("karthik@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div[2]/div/form/button").click()


except:


    driver.find_element(By.ID, "email").send_keys("karthik@gmail.com")
    driver.find_element(By.XPATH, "//a[@data-testid='login-continue']").click()

# driver.find_element(By.XPATH,"//*[@id='lm-cookie-wall-container']").click()
# time.sleep(10)

# driver.find_element(By.ID,"email").send_keys("karthik@gmail.com")

# driver.find_element(By.XPATH,"//a[@data-testid='login-continue']").click()
# time.sleep(3)

# driver.find_element(By.NAME,"btnK").click()
# time.sleep(3)

driver.close()
print("sample test successfully completed")
