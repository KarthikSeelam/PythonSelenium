import time
import pandas as pd
from selenium import webdriver
import mysql.connector
from selenium.webdriver.common.by import By

print("sample test started")
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://nypcml07zqdw4ioh21app.ecwcloud.com/mobiledoc/jsp/webemr/login/newLogin.jsp#/mobiledoc/jsp/webemr/scheduling/resourceSchedule.jsp/%7B%22providerId%22:%229180%22%7D")
time.sleep(5)
username = driver.find_element(By.XPATH, "//input[@id='doctorID']")
username.send_keys("CHDATA02")
time.sleep(5)

next_button_for_password = driver.find_element(By.XPATH, "//input[@id='nextStep']")
next_button_for_password.click()
time.sleep(5)
password = driver.find_element(By.XPATH, "//input[@id='passwordField']")
password.send_keys("Newpass5!")
time.sleep(5)
login_button = driver.find_element(By.XPATH, "//input[@id='Login']")
login_button.click()

time.sleep(5)
try:
    security_modal_popup = driver.find_element(By.XPATH, "//button[@onclick='closeSecModal()']")
    security_modal_popup.click()
except:
    time.sleep(5)

side_panel = driver.find_element(By.XPATH, "//a[@id='jellybean-panelLink4']")
side_panel.click()
time.sleep(4)

billing_button = driver.find_element(By.XPATH, "//li[@title='Billing']/a")
billing_button.click()
time.sleep(4)
claims_button_in_billing = driver.find_element(By.XPATH, "//li[@title='Billing']/div/div/ul/li[3]")
claims_button_in_billing.click()
time.sleep(10)
service_fromDate = driver.find_element(By.XPATH,"//*[@id='fromdate']")
service_fromDate.click()
service_fromDate.send_keys("01/01/2022")
time.sleep(3)
service_toDate = driver.find_element(By.XPATH,"//*[@id='todate']")
service_toDate.click()
service_toDate.send_keys("12/31/2022")
time.sleep(3)
claim_status = driver.find_element(By.XPATH, "//*[@id='claimStatusCodeId']/option[3]")
claim_status.click()
claim_number = driver.find_element(By.XPATH,"//*[@id='claimLookupIpt10']")
claim_number.send_keys("67220")
lookup = driver.find_element(By.XPATH,"//*[@id='btnclaimlookup']")
lookup.click()
time.sleep(20)
facilityList = driver.find_element(By.XPATH, "//*[@id='billingClaimBtn4']")
facilityList.click()
time.sleep(5)
facility_data = []
while True:
    facility_table = driver.find_elements(By.XPATH, "//*[@id='facilityListTbl']/tbody/tr")
    for row in facility_table:

        facility_name = row.find_element(By.XPATH, "./td[2]").text
        facility_code = row.find_element(By.XPATH, "./td[3]").text
        city = row.find_element(By.XPATH, "./td[4]").text
        state = row.find_element(By.XPATH, "./td[5]").text
        zip_code = row.find_element(By.XPATH, "./td[6]").text
        telephone = row.find_element(By.XPATH, "./td[7]").text
        fax = row.find_element(By.XPATH, "./td[8]").text
        email = row.find_element(By.XPATH, "./td[9]/span").text
        if "TeleHealth" in facility_name:
            pos = "02"
        elif "Home Testing" in facility_name:
            pos = "12"
        elif "Testing Center" in facility_name or "Urgent Care" in facility_name:
            pos = "20"
        else:
            pos = ""

        facility_data.append({

            "Facility Name": facility_name,
            "Facility Code": facility_code,
            "City": city,
            "State": state,
            "Zip Code": zip_code,
            "Telephone": telephone,
            "Fax": fax,
            "Email": email,
            "POS":pos
        })

    next_button = driver.find_element(By.XPATH, "//*[@id='nextID']")
    if next_button.get_attribute("disabled") == "true":
        break
    else:
        next_button.click()
        time.sleep(3)
df = pd.DataFrame(facility_data)
print(df)
facilityName = driver.find_element(By.XPATH,"//*[@id='billingClaimIpt23']")
printName = facilityName.get_attribute('value')
print(printName)
pos= driver.find_element(By.XPATH,"//*[@id='billingClaimIpt24']")
serviceCode = pos.get_attribute('value')
print(serviceCode)
icd_code = driver.find_element(By.XPATH,"//*[@id='billingClaimIpt2ngR0']").get_attribute('value')
print(icd_code)
insurance = driver.find_element(By.XPATH,"//*[@id='billingClaimTbl5']/tbody/tr/td[2]/sapn").text
print("Insurance: ", insurance)
cptData = []
cpt_table = driver.find_elements(By.XPATH, "//*[@id='claimCPTCodesTable1689677624788']/tbody/tr")
for cptRows in cpt_table:
    cptCode = cptRows.find_element(By.XPATH, "./td[3]").get_attribute("value")
    modifier = cptRows.find_element(By.XPATH, "./td[8]").get_attribute("value")
    cptData.append({
        "CPT CODE ": cptCode,
        "Modifier": modifier
    })
df2 = pd.DataFrame(cptData)
print(df2)
driver.close()


print("sample test successfully completed")
