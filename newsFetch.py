from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.support.ui as UI
import time
import json
import csv

driver=webdriver.Chrome()
i = 0;

with open('news3.csv','ab') as csvfile:
    fieldnames = ['Date','Title','Description'];
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames);
    writer.writeheader();
    for year in range(2010,2014):
        for page in range(1,15):
            driver.get("http://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=PNB05&scat=&pageno="+str(page)+"&next=0&durationType=Y&Year="+str(year)+"&duration=1&news_type=");
            elements = driver.find_elements_by_xpath("//div[contains(@class, 'MT15 PT10 PB10')]");
            if(len(elements) != 0):
                for span in elements:
                    splits = span.text.split('|');
                    spLen = len(splits);
                    if(spLen > 1):
                        title = str(splits[0].encode("utf-8")).split("\n")[0];
                        date = str(splits[1].encode("utf-8"));
                        description = str(splits[2].encode("utf-8").split("\n")[1]);

                        print("\nNEWS : "+str(i));
                        print("TITLE : "+title);
                        print("DESCRIPTION : "+description);
                        print("DATE : "+date);

                        writer.writerow({'Date':date,'Title':title,'Description':description});
                        i = i + 1;

driver.quit();
