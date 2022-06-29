import os

import selenium.common.exceptions
import undetected_chromedriver.v2 as uc
from time import sleep
from os import system
from user import lost
import random
mn=0
mm=0
print(f'We Have {len(lost)} EMAIL.')
if __name__ == '__main__':
    while mm<len(lost):
        def dele():
            os.remove("youtube.py")
            main()
        def main():
            global chos,link,user,passs,mm
            link = input("Enter link Video OR Channel\n>>")
            chos=input("""
Choose From list:
    [1] subscribe from account -> One Time
    [2] Subscribe From Account -> 2 Times
>> """)


            if chos== "1":
                signin()
            elif chos=="2":
                signin()
            else:
                print("I didn't Get Correct ANSWER")
                main()
        def signin():
            global driver, link, mm
            i = [mm]
            element1 = []
            for index in i:
                try:
                    element1.append(lost[index])
                except IndexError:
                    print("All Account IS Done Scripted BY: OmarElDab3")
                    quit()
            for element2 in element1:
                user = element2.split(":")[0]
                passs = element2.split(":")[1]
                pass
            username =user
            password =passs

            #link=input("Enter link Video OR Channel\n>>")
            driver = uc.Chrome()
            driver.delete_all_cookies()
            print(f"{mm} EMAIL IS: {username}")
            driver.get('https://accounts.google.com/ServiceLogin?hl=en')
            #sleep(3)
            driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
            driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
            sleep(5)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
            sleep(8)
            try:
                driver.find_element_by_xpath('//*[@data-challengetype="12"]').click()
                rec=open("recov.py","r").read()
                sleep(5)
                driver.find_element_by_xpath('//input[@aria-label="Enter recovery email address"]').send_keys(rec)
                driver.find_element_by_xpath('//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b"]').click()
                print("TEST IS DONE")
                sleep(5)
            except:
                try:
                    driver.find_element_by_xpath('//a[@class="NEHYte uU7LXe WkkcEb EhlvJf"]')
                    print("NO RECOVRERY MAIL NEED")
                except:
                    system("cls")
                    sleep(5)
                    print(f"Error Found recovery MAil In: {username}")
                    eror=open("Errors.py","r").read()
                    if username not in eror:
                        open("Errors.py","a+").write(f"{username},\n")
                    else:
                        print("email already error")
                        pass
                    mm+=1
                    driver.close()
                    signin()

            #driver.get(link)
            #sleep(25)
            #driver.find_element_by_xpath('//*[@id="subscribe-button"]').click()
            #sleep(5) https://www.youtube.com/watch?v=W-Xk4ZUW-ko
            if chos=="1":
                sub()
            if chos=="2":
                crch()
        def sub():
            global mm
            i = [mm]
            element1 = []
            for index in i:
                element1.append(lost[index])
            for element2 in element1:
                user = element2.split(":")[0]
                passs = element2.split(":")[1]
                pass
            driver.get(link)
            sleep(10)
            driver.find_element_by_xpath('//tp-yt-paper-button[@class="style-scope ytd-subscribe-button-renderer"]').click()
            system("cls")
            print("Done Set Subscribe 1 TIme Good Bye")
            sleep(15)
            mm+=1
            driver.close()
            signin()
        def crch():
            global mn,mm
            while mn<2:
                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                us = str("".join(random.choice(chars) for i in range(8)))
                namechannel=f"{us}"
                driver.get("https://www.youtube.com/create_channel?action_create_new_channel_redirect=true")
                sleep(3)
                driver.find_element_by_xpath('//input[@id="PlusPageName"]').send_keys(namechannel)
                driver.find_element_by_xpath('//span[@class="consent-checkmark"]').click()
                driver.find_element_by_xpath('//input[@id="submitbutton"]').click()
                sleep(4)
                driver.get(link)
                sleep(15)
                #input("Enter")
                driver.find_element_by_xpath('//tp-yt-paper-button[@class="style-scope ytd-subscribe-button-renderer"]').click()
                #driver.find_element_by_xpath('//yt-icon[@class="style-scope ytd-toggle-button-renderer"]').click()
                system("cls")
                print(f"Done Set {mn} Subscribe Sleep (15) second")
                sleep(15)
                mn+=1
                crch()
            if mn==2 and mm != len(lost):
                #
                print(f"Done Set Subscribe 2 TImes, ")
                sleep(10)

                driver.close()
                mm += 1
                mn-=2
                signin()
            if mn==2 and mm == len(lost):
                print(f"Done Set Subscribe 2 TImes, Good Bye")
                sleep(10)
                mm+=1
        dele()
