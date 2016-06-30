'''
This file will be used to calculate anything that has to do with logistics

func unitsAvailableNow(donor) ##function returns how many units are available now
return donor.materialAvailable



func unitsAvailable(DonorID, date) ##function returns how many units will be available at a future date (estimated)
 - Must be future date
 time = calculate number of weeks between today and input date
 new product = time*donor.productionRate
 total product = materialAvailable + new product


func willBeAvailable(units, DonorID, date) ##function returns if a certain number of units will be available date (estimated)
-must be future date
 time = calculate number of weeks between today and input date
 new product = time*donor.productionRate
 total product = materialAvailable + new product
 if totalProduct>units
 return true
 else
 return false

func dateAvailable(units, DonorID) ##function returns date a certain number of units will be available (estimated)
new units = untis - donor.materialAvailable
time = new units / donor.productionRate
date = time + today
return date
'''

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://id.heroku.com/login')
email = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
loginButton = browser.find_element_by_name("commit")

email.send_keys("alim@openbiome.org")
password.send_keys("Wolfpuck1!")
loginButton.click()
browser.get('https://dataclips.heroku.com/xuxyyihpajhswmajwsfgewefelws-donor-stats')
time.sleep(5)
browser.get('https://dataclips.heroku.com/xuxyyihpajhswmajwsfgewefelws-donor-stats.json')
elem = browser.find_element_by_tag_name("pre")
content = elem.text
print content
