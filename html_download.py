import os
import requests
import sys


def code_html():
    for year in range(2013,2019): # data from 2013-2018 included
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)  #for month 1-9
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)    #for months 10-12
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
if __name__=="__main__":
    code_html()
        
