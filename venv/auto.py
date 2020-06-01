from selenium import webdriver
import time
browser=webdriver.Edge(executable_path='C:\Setups\msedgedriver') #path where the edge driver in my system is saved
browser.get("https://web.whatsapp.com/")                         #used "Edge" for microsoft edge browser will change accordingly if any other browser is used
time.sleep(10)

sender=input("Enter the recipent")                               #name of the recipent
find=browser.find_element_by_xpath('//div[@title="New chat"]')
find.click()
find1=browser.find_element_by_xpath('//div[@dir="ltr"]')
find1.click()
find1.send_keys(sender)



send=browser.find_element_by_xpath('//span[@title="{}"]'.format(sender))
send.click()

n=int(input("Enter the number of times you want to send the message"))  #the count of the text
message=input("Enter the message")                                      #the message

for i in range(n):
    box=browser.find_element_by_xpath('//div[@class="_1Plpp"]')
    box.send_keys(message)
    arrow=browser.find_element_by_xpath('//button[@class="_35EW6"]')
    arrow.click()