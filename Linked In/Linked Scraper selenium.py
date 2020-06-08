# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:31:57 2020

@author: Yadnesh
"""

#Importing packages
from selenium import webdriver
import pandas as pd
from parsel import Selector


main_url="https://www.linkedin.com/login"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(main_url)

# locate email form by_class_name
username = driver.find_element_by_id('username')


# send_keys() to simulate key strokes
username.send_keys('XXXXX@gmail.com')
#sleep(0.5)


# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('XXXX')


# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()

driver.execute_script("window.open();")
add_url="detail/contact-info/"
profile_url="https://www.linkedin.com/in/yadneshc/"
tab_url=profile_url+add_url
driver.get(tab_url)

#driver.execute_script("window.open('"+tab_url+"', 'new_window')")


sel = Selector(text=driver.page_source) 
#xpath to extract the first h1 text 
name = sel.xpath('//h1/text()').extract_first()
email = sel.xpath('/html/body/div[4]/div/div/div[2]/section/div/div[1]/div/section[3]/div/a/text()').extract_first()


a_list = name.split()

name = " ".join(a_list)

a_list = email.split()

email = " ".join(a_list)

print("Link : "+profile_url+"\nName : "+name+"\nEmail : "+email)
