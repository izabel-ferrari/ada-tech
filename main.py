# -*- coding: utf-8 -*-

from csv import DictReader
from extract_walmart import walmart
from extract_amazon import amazon
from extract_google import google

if __name__ == '__main__':

    with open('listproducts.csv', 'r') as read_obj:
        csv_dict_reader = DictReader(read_obj)

        for row in csv_dict_reader:
            site=row['site']
            product=row['product']
            url=row['url']
            print("---------------------------")
            print("Site: "+site)
            print("Product: " + product)
            print("Url:" + url)
            print("---------------------------")
            
            print("Beginning scraping-"+site)
            
            if site=='google':                
                google(url,product)
                #print("google")
            elif site=='walmart':
                walmart(url,product)
                #print("walmart")
            elif site=='amazon':
                amazon(url, product)
                #print("amazon")
                
            print("Finished scraping-"+site)