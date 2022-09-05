import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from datetime import date
import calendar


def file_creation():
    Name = input("Enter Your Name - ")
    MyEmail = input("Enter You MS-Teams EMAIL ID - ")
    MyPass = input("Enter You MS-Teams EMAIL PASSWORD - ")
    f = open("account.txt","w+")
    f.write("--- NAME ---\n")
    f.write(Name)
    f.write("\n")
    f.write("--- EMAIL ID ---\n")
    f.write(MyEmail)
    f.write("\n")
    f.write("--- PASSWORD ---\n")
    f.write(MyPass)
    f.write("\n")
    f.close()

def file_access():
    f = open("account.txt","r+")
    lines = f.readlines()
    Name = lines[1]
    MyEmail = lines[3]
    MyPass = lines[5]
    f.close()
    return [Name,MyEmail,MyPass]


def LoginBot():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.microsoft.com/en-in/microsoft-teams/group-chat-software')

    # Opens the teams page and wait 5 sec
    time.sleep(3)


    # Clicks on Sign In 
    element = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/main/div/div/div/div[2]/div/div/div/section/div/div/div[1]/div/div[2]/div[2]/a')
    element.click()


    # Switches to the new login tab.
    new_window = driver.window_handles
    driver.switch_to.window(new_window[1])
    time.sleep(7)


    # Fills the EMAIL Address
    element = driver.find_element_by_xpath('//*[@id="i0116"]')
    element.send_keys(list[1])
    time.sleep(3)

    # Clicks Next
    element = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    element.click()
    time.sleep(3)

    # Fills the Passworrd
    element = driver.find_element_by_xpath('//*[@id="i0118"]')
    element.send_keys(list[2])
    time.sleep(3)

    # Submits the login in form
    element = driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    element.click()
    time.sleep(3)

    # Clicking "Don't Save Password"
    text = driver.find_element_by_xpath('//*[@id="lightbox"]/div[3]/div/div[2]/div/div[1]').text
    if text == "Stay signed in?" :
        driver.find_element_by_xpath('//*[@id="idBtn_Back"]').click()
        time.sleep(10)

    driver.switch_to.window(new_window[1])
    time.sleep(5)
    driver. close() 

file_check = os.path.isfile("account.txt")

while True:
    print("\n\n** NOTE ***")
    print("\nFOR FIRST TIME MAKE SURE TO CHOOSE OPTION 2\n")
    print("---- OPTIONS ----")
    print("Press 1 to continue with OLD ACCOUNT file")
    print("Press 2 to make new ACCOUNT file")

    n = input("YOUR CHOICE - ")
    if n.isdigit():
        n = int(n)
        if n == 1 :

            if file_check == True:
                list = file_access()
                LoginBot()

            if file_check == False:
                file_creation()
                list = file_access()
                LoginBot()
            break

        elif n == 2:
            
            if file_check == True :
                os.remove('account.txt')
            
            file_creation()
            list = file_access()
            LoginBot()
            
            break

    elif type(n) == str:
        print('''
        *ERROR*
        INVALID RE-ENTER INTEGER INPUT
        ''')
        
    else:
        print('''
        *ERROR*
        INVALID RE-ENTER INTEGER INPUT
        ''')
        

today = datetime.datetime.now()
current_time = today.strftime("%H:%M")
current_date = date.today()
current_day = calendar.day_name[current_date.weekday()]
print("DATE = ", current_date, "\nTIME = ",current_time, "\nDAY = ",current_day,"\n--- Welcome ---" , list[0], sep='')
print("WELL DONE YOU ARE IN YOUR MS TEAMS ACCOUNT ")

