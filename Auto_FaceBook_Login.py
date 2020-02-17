from selenium import webdriver
import pyautogui
import sys
import time
file=open('D://Person//Facebook.csv','a')
driver=webdriver.Chrome('C:\\Users\\Gowtham\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.facebook.com')
us=driver.find_element_by_id('email')
us.send_keys('my_gmail_id')
pa=driver.find_element_by_id('pass')
pa.send_keys('my_password')
cl=driver.find_element_by_xpath("//form[@id='login_form']/input[3]")
cl.submit()
b=pyautogui.locateOnScreen('D://facebook_notif_block.png')
pyautogui.click(b)
a=input('Enter quit if you want to close WebDriver/t ')
if(a=='quit'):
    a=pyautogui.locateOnScreen('D://drop.png')
    print('Found Drop down list box for Log out')
    print(a)
    pyautogui.click(a)
    time.sleep(3)
    a=pyautogui.locateOnScreen('D://LogOut.png')
    print('Found Log Out button for Log out')
    print(a)
    pyautogui.click(a)
    print('facebook is signing out')
    driver.close()

