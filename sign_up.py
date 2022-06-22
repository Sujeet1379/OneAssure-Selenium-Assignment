from selenium import webdriver  #Import Webdriver
import time


def createGoogleAcoountPage(driver ) :
    """Creating New Account"""

    firstname = driver.find_element_by_id("firstName")
    firstname.send_keys("Test")     #Enter First Name
    lastname = driver.find_element_by_id("lastName")
    lastname.send_keys("One")     #Enter Last Name
    username = driver.find_element_by_id("username")
    username.send_keys("test1.one@gmail.com")    #Enter Email
    password = driver.find_element_by_name("Passwd")
    password.send_keys("test1245@")     #Enter Password
    confirm = driver.find_element_by_name ("ConfirmPasswd")
    confirm.send_keys("test1245@")     #Confirm Password

    #Submit form Button
    next_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    next_Button.click()

def verifyPhoneNumber(driver) :
    phone_number=driver.find_element_by_tag_name("input")
    phone_number.send_keys("7023360000")   #Enter Phone Number

    next_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[0]
    next_Button.click()

def verifyCode(driver) :
    time.sleep(30)
    
    """Enter OTP to verify in  chrome UI manualy"""

    verify_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    verify_Button.click()

def welcomePage(driver) :
    """Date of Birth And Gender Part"""

    day = driver.find_element_by_xpath('//*[@id="day"]')
    day.send_keys("24")       #Enter Day
    year = driver.find_element_by_xpath('//*[@id="year"]')
    year.send_keys("2001")       #Enter Year
    month = driver.find_elements_by_class_name("UDCCJb")[0]
    month.send_keys("June")    #Enter Month
    gender = driver.find_elements_by_class_name("UDCCJb")[1]
    gender.send_keys("Male")   #Enter Gender

    #Submit Button
    next_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[0]
    next_Button.click()

def morefromNumberPage(driver):
    """Term & Condition Part"""
    
    yes_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    yes_Button.click()
    

def PrivacyandTermPage(driver):
    """Term & Condition Part"""

    agree_Button = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    agree_Button.click()





driver = webdriver.Chrome(executable_path="./chromedriver.exe") #Webdriver Path

#implicit wait
driver.implicitly_wait(0.5)


#launch URL
driver.get("https://accounts.google.com/signup")


"""Calling Functions"""
createGoogleAcoountPage(driver)
time.sleep(4)

verifyPhoneNumber(driver)
time.sleep(4)

verifyCode(driver)
time.sleep(4)

welcomePage(driver)
time.sleep(4)

morefromNumberPage(driver)
time.sleep(4)


PrivacyandTermPage(driver)
time.sleep(15)

