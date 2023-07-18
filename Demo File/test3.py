from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class testing_web_element():

    def demo_select(self):
        driver = webdriver.Chrome()

        ##driver.get("https://contractbook.com/")
        ##driver.get("https://phptravels.com/demo/")
        ##driver.get("https://accounts.zoho.in/signin?servicename=VirtualOffice&signupurl=https://www.zoho.in/mail/zohomail-pricing.html&serviceurl=https://mail.zoho.in")
        #driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.get("https://www.yatra.com/")

        driver.maximize_window()

        time.sleep(2)

        ##driver.find_element(By.XPATH, "//a[@data-text-name='integrations']//self::a").click()
        ##print('In axes self')



        #dropdown = driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']")
        #dd = Select(dropdown)
        #dd.select_by_value('IT_Manager_AP')
        #dd.select_by_index(4)
        #dd.select_by_visible_text('Marketing / PR Manager')
        ##like wise we can use for the multiselect element also
        #mail
        #driver.find_element(By.CSS_SELECTOR, "input#login_id").send_keys('test@gmail.com')
        # cont
        #driver.find_element(By.CSS_SELECTOR, "div.p-16").click()
        # mail
        # driver.find_element(By.CSS_SELECTOR, "button#nextbtn[class = 'btn blue'][tabindex= '2']").click()

        # yatra
        # driver.find_element(By.CSS_SELECTOR, "a[id^= booking_engine_hote]").click() #prefix
        # driver.find_element(By.CSS_SELECTOR, "a[id$= engine_hotels]").click()  #suffix
       # driver.find_element(By.CSS_SELECTOR, "a[id*= engine_hote]").click()  #substring\

        driver.find_element(By.CSS_SELECTOR, "div[class = 'oneway-roundtrip']>ul").click() #child(Parent) sign is > here

        # driver.find_element(By.CSS_SELECTOR, "div[class = 'oneway-roundtrip'] li").click() # subchild(child+grandchild) sign is space here

        # driver.find_element(By.CSS_SELECTOR, "ul[class='be-tabs-snipe clearfix']>li+li").click() # next sibling (immediately follow here) sing is + here

        # driver.find_element(By.CSS_SELECTOR, "ul[class='be-tabs-snipe clearfix']>:first-child").click() # first child sign is >:first-child here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>:last-child").click() # first child sign is >:last-child here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>:nth-child(2)").click() # nth child sign is >:nth-child here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>:nth-last-child(2)").click() # nth last child sign is >:nth-last-child here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>li:first-of-type").click() # first-of-type sign is :first-of-type here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>li:last-of-type").click() # last-of-type sign is :last-of-type here

        # driver.find_element(By.CSS_SELECTOR, "ul[class="be-tabs-snipe clearfix"]>li:nth-of-type(3)").click() # nth of type sign is :nth-of-type(3) here
        time.sleep(5)

        driver.quit()


element = testing_web_element()

element.demo_select()



