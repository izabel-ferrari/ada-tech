# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
from random import randint
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def walmart(url,product):
    #chrome_path = os.path.realpath('chromedriver.exe')
    #driver = webdriver.Chrome(executable_path=chrome_path)
    driver = webdriver.Chrome()
    driver.get(url)
    count=2
    
    file_name="walmart_reviews_"+product+".csv"
    print("Creating csv file - reviews: " +file_name)
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["*************************************"])
        writer.writerow([product])
        writer.writerow([url])
        writer.writerow(["*************************************"])
        count=1
        
        while True:  
            try:
                #Check if there is the next page
                driver.find_element_by_xpath("//button[contains(@class, 'paginator-btn-next')]")
            except NoSuchElementException:
                print("There is no next page.")
                break
            
            try:
                #Get all reviews
                element_list=driver.find_elements_by_xpath("//div[@class='review-text']/p")
                for item in element_list:
                    writer.writerow([item.text.strip()])
            except NoSuchElementException:
                print("There is no review.")
                
            count=count+1
            url_review=''
            url_review=url+"?page="+str(count)
            print("Url:" +url_review)
            driver.get(url_review)
            sleep(randint(5,15))
    
    driver.close()
         
    
    
