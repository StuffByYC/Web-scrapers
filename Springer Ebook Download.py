# -*- coding: utf-8 -*-
"""
Created on Tue May 12 14:29:41 2020

@author: Yadnesh

https://www.stuffbyyc.com/
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import re


data =  pd.read_csv("Data/Springer Ebooks.csv") 
Book_Title = data.Book_Title.tolist()
OpenURL = data.OpenURL.tolist()

for i in range(len(Book_Title)):
    url = OpenURL[i]
    filename= Book_Title[i]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    #Getting Download link
    for link in soup.findAll("a",class_ = "c-button c-button--blue c-button__icon-right test-download-book-options test-bookpdf-link", attrs={'href': re.compile("content/pdf/")}):
        print(link.get('href'))
        download_lnk=link.get('href')
        
    
    file_url = "https://link.springer.com"+str(download_lnk)


    myfile = requests.get(file_url)
    open("Downloads/"+filename+".pdf", 'wb').write(myfile.content)
    
    
    