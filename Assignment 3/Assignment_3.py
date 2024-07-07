# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up webdriver
driver = webdriver.Chrome()

# Navigating to https://www.conestogac.on.ca/
driver.get("https://www.conestogac.on.ca/")
time.sleep(2)

# Maximize browser window
driver.maximize_window()

# Clicking on programs-and-courses menu
programs_and_courses = driver.find_element("xpath","/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/a[1]")
programs_and_courses.click()
time.sleep(2)

# Clicking on Full-Time Programs button
full_time_programs = driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div/div[1]/a")
full_time_programs.click()
time.sleep(2)

# Selecting International students checkbox
international_students = driver.find_element("id","DeliveryGroups")
international_students.click()
time.sleep(2)

# Clicking on Apply filters button
apply_filters = driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div/div/div[2]/form/div/div[3]/div/div[1]/div[3]/div[1]/button/span/span[1]")
apply_filters.click()
time.sleep(2)

# Clicking on first program in the filtered results
first_program = driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div/div/ul/li[1]/a/span/span[1]")
first_program.click()
time.sleep(2)

# Clicking on Admissions tab
admissions = driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div/ul/li[2]/a")
admissions.click()
time.sleep(2)

# Clicking on Apply Now
apply_now = driver.find_element("xpath","/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[1]/button/span")
apply_now.click()
time.sleep(2)

# Closing the webdriver
#driver.close()
