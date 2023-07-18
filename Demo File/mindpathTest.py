from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

print("sample test started")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://ican-manage-mindpath-tst.cognitivehealthit.com/CashManagement/")

userName = driver.find_element(By.ID, "username")
userName.send_keys("Sravanth.t@cognitivehealthit.com")

passWord = driver.find_element(By.ID, "password")
passWord.send_keys("test12345")

loginButton = driver.find_element(By.NAME, "submit")
loginButton.click()

time.sleep(10)



class mindpath_test():
    def cash_management_page(self):
        dropdown_toggle = driver.find_element(By.XPATH,
                                              "//button[@class='btn dropdown-toggle btn-default statusClearValues']")
        dropdown_toggle.click()
        time.sleep(5)
        deselect_all_button = driver.find_element(By.XPATH,
                                                  "//button[contains(@class,'statusSelectDeselectClear') and contains(text(), 'DeSelect All')]")
        deselect_all_button.click()
        time.sleep(5)
        hospitalList = driver.find_elements(By.XPATH, "//ul[contains(@class, 'hospitalNamesListCls')]")
        first_hospital = hospitalList[0].find_element(By.TAG_NAME, 'li')

        # Click on the first <li> tag
        first_hospital.click()
        time.sleep(5)
        print(len(hospitalList))
        for hospitalNames in hospitalList:
            hospitals = hospitalNames.find_elements(By.TAG_NAME, 'li')
            for hospital in hospitals:
                hospital_id = hospital.get_attribute('attr_hospital_id')
                hospital_name = hospital.text
                print(f"Hospital ID: {hospital_id}, Hospital Name: {hospital_name}")

                hospital.click()
                time.sleep(15)

                total_deposits_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalDepositsId'))
                )
                total_remittances_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalRemmitancesId'))
                )
                total_posting_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalEpicPostingId'))
                )
                total_variance_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalVarianceId'))
                )
                total_notposted_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalNotPostedId'))
                )

                # Retrieve the total deposits text
                total_deposits = total_deposits_element.text
                total_remittances = total_remittances_element.text
                total_posting = total_posting_element.text
                total_variance = total_variance_element.text
                total_notposted = total_notposted_element.text
                print(f"Total Deposits: {total_deposits}")
                print(f"Total Remittances: {total_remittances}")
                print(f"Total Epic Posting: {total_posting}")
                print(f"Total Variance: {total_variance}")
                print(f"Total Not Posted: {total_notposted}")

        time.sleep(5)

    def reconciled_page(self):
        reconciled_element = driver.find_element(By.XPATH,
                                                 "//a[contains(@class, 'clearfix') and @href='/CashManagement/historical-page-work-queue']")
        reconciled_element.click()
        time.sleep(10)
        hospitallist = driver.find_elements(By.XPATH, "//ul[contains(@class, 'hospitalNamesListCls')]")
        first_hospital = hospitallist[0].find_element(By.TAG_NAME, 'li')

        # Click on the first <li> tag
        first_hospital.click()
        time.sleep(10)
        for hospitalNames in hospitallist:
            hospitals = hospitalNames.find_elements(By.TAG_NAME, 'li')
            for hospital in hospitals:
                hospital_id = hospital.get_attribute('attr_hospital_id')
                hospital_name = hospital.text
                print(f"Hospital ID: {hospital_id}, Hospital Name: {hospital_name}")

                hospital.click()
                time.sleep(15)

                total_deposits_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalDepositsId'))
                )
                total_remittances_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalRemmitancesId'))
                )
                total_posting_element = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.ID, 'totalEpicPostingId'))
                )


                # Retrieve the total deposits text
                total_deposits = total_deposits_element.text
                total_remittances = total_remittances_element.text
                total_posting = total_posting_element.text

                print(f"Total Deposits: {total_deposits}")
                print(f"Total Remittances: {total_remittances}")
                print(f"Total Epic Posting: {total_posting}")

        time.sleep(5)

element = mindpath_test()
#element.cash_management_page()
time.sleep(10)
element.reconciled_page()
time.sleep(10)
driver.close()
print("sample test successfully completed")
