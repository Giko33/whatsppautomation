#install selenium first using pip
from selenium import webdriver


#required for getting enough time for scanning
import time


#path where the edge driver in the concerned system is saved
#used "Edge" for microsoft edge browser will change accordingly
browser=webdriver.Edge(executable_path='C:\Setups\msedgedriver')
browser.get("https://web.whatsapp.com/")
time.sleep(10)

# name of the recipent
sender=input("Enter the recipent")

#the location in the web browser where the new chat option of the whatsapp is situated
#then click it
find=browser.find_element_by_xpath('//div[@title="New chat"]')
find.click()

#location of the search bar in whatsapp
find1=browser.find_element_by_xpath('//div[@dir="ltr"]')
find1.click()
find1.send_keys(sender)


#clicking on the name of the recipent
#clicking it then
send=browser.find_element_by_xpath('//span[@title="{}"]'.format(sender))
send.click()

#the number of times the message is needed to be spent
n=int(input("Enter the number of times you want to send the message"))

#the message to be sent
message=input("Enter the message")


#the type your message area in whatsapp
#then clicking the arrow for sending
for i in range(n):
    box=browser.find_element_by_xpath('//div[@class="_1Plpp"]')
    box.send_keys(message)
    arrow=browser.find_element_by_xpath('//button[@class="_35EW6"]')
    arrow.click()