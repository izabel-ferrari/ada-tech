# -*- coding: utf-8 -*-

from selenium import webdriver
from random import randint
from time import sleep
import csv
from selenium.common.exceptions import NoSuchElementException

def ClickAllTranslateButton(driver):
    elements_translate= driver.find_elements_by_xpath("//div[contains(@data-snippit-class-prefix, 'sg-review')]")
    for item in elements_translate:
        webdriver.ActionChains(driver).move_to_element(item).click(item).perform()
        sleep(randint(1,5))

def google(url,product):
    #chrome_path = os.path.realpath('chromedriver.exe')
    #driver = webdriver.Chrome(executable_path=chrome_path)
    driver = webdriver.Chrome()
    driver.get(url)
    
    total_reviews = driver.find_element_by_xpath("//span[contains(@class, 'HiT7Id')]/span")
    
   
    while True:
        try:
            #Search "More reviews" button and click
            element = driver.find_element_by_xpath("//button[contains(@class, 'pagination-button')]")
            element.click()
            sleep(randint(1,15))
        except NoSuchElementException:
            print("There is no reviews.")
            break
  
    ClickAllTranslateButton(driver)
    
    #Get all reviews (visible and hidden)
    comment_list = driver.find_elements_by_xpath("//*[contains(@id, '-full')]")
    #Get all reviews visible
    onlyVisible = filter(lambda x: x.is_displayed(), comment_list)    
    
    file_name="google_reviews_"+product+".csv"
    print("Creating csv file - reviews: " +file_name)
    
    # Create a csv file and add reviews
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["*************************************"])
        writer.writerow([product])
        writer.writerow([url])
        writer.writerow([total_reviews])
        writer.writerow(["*************************************"])
        for item in onlyVisible:
            if item.text!="Show in original language":
                writer.writerow([item.text.strip()])
    
    driver.close()
    