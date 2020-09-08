# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import csv
from random import randint
from time import sleep
import logging
from selenium.common.exceptions import NoSuchElementException

def ClickAllTranslateButton(driver):
    element_translate = driver.find_element_by_xpath("//a[contains(@data-hook, 'cr-translate-these-reviews-link')]")
    webdriver.ActionChains(driver).move_to_element(element_translate).click(element_translate).perform()
    #element_translate.click()

def amazon(url,product):
    chrome_path = os.path.realpath('chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver = webdriver.Chrome()
    driver.get(url)
    
    try:
        ClickAllTranslateButton(driver)
    except NoSuchElementException:
        logging.info("There is no translate button.")
        

    file_name="amazon_reviews_"+product+".csv"    
    logging.info("Creating csv file - reviews: " +file_name)
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["*************************************"])
        writer.writerow([product])
        writer.writerow([url])
        writer.writerow(["*************************************"])
        count=2
    
        while True:  
            try:
                comment_list=driver.find_elements_by_xpath("//span[@data-hook='review-body']/span")
            except NoSuchElementException:
                logging.info("There is no review.")
                break
               
            for item in comment_list:
                writer.writerow([item.text.strip()])
               
            #Check if there is the next page
            try: 
                element=driver.find_element_by_xpath("//li[@class='a-last']/a")
            except NoSuchElementException:
                logging.info("There is no next page.")
                break
    
            url_review=""
            url_review=url+"/ref=cm_cr_getr_d_paging_btm_"+str(count)+"?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(count)
            logging.info("Url:" +url_review)
            driver.get(url_review)
            sleep(randint(5,15))
            count=count+1
    
    driver.close()