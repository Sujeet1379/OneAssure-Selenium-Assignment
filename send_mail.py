from selenium import webdriver  #Import Webdriver
import time


def enterMail(driver ) :
    """Enter Email Part"""
    firstname = driver.find_element_by_id("identifierId")
    firstname.send_keys("test1.one@gmail.com")  #Enter Email
    
    time.sleep(2)
    nextButton = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    nextButton.click()



    # time.sleep(20)
    # nextButton = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    # nextButton.click()


    
def enterPassword(driver ) :
    """Enter Password Part"""

    firstname = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    firstname.send_keys("Password@123")   #Enter Password

    nextButton = driver.find_elements_by_class_name("VfPpkd-vQzf8d")[1]
    nextButton.click()
    time.sleep(10)



def sendMail(driver):
    driver.find_element_by_xpath('//*[@id=":3m"]/div/div').click()
    time.sleep(2)
    to = driver.find_element_by_xpath('//*[@id=":93"]/div')
    to.send_keys("tech@oneassure.in")    #Enter Receiver Mail
    time.sleep(2)
    subject=driver.find_element_by_name('subjectbox')
    subject.send_keys("OneAssure Selenium Assignment")  #Enter Subject
    time.sleep(2)
    text=driver.find_elements_by_xpath('Am Al editable LW-avf tS-tW')[0]
    text.send_keys(" Hi,\n This is an email generated from selenium.\n\n Regards,\n Test One")  #Enter Your Message
    time.sleep(2)

    #Click on Send
    send=driver.find_element_by_xpath('//*[@id=":7o"]')
    send.click()


driver = webdriver.Chrome(executable_path="./chromedriver.exe")    #Webdriver Path
#implicit wait
driver.implicitly_wait(1)

#launch URL
driver.get("https://mail.google.com/")
time.sleep(3)

"""Calling Functions"""
enterMail(driver)
time.sleep(3)

enterPassword(driver)
time.sleep(15)

sendMail(driver)
time.sleep(10)


