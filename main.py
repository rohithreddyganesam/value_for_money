import requests
import bs4
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime
import os
import time
url = 'https://www.amazon.in/PS5-Grand-Theft-Auto-V/dp/B09XJ8FGVP/ref=sr_1_1?crid=2XPG1IE840LIW&keywords=gta+5+ps5&qid=1679299722&sprefix=gta5+ps5%2Caps%2C232&sr=8-1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
def check_our_price():
    page=requests.get(url,headers=headers)
    bs=BeautifulSoup(page.content,'html.parser')
    #print(bs.prettify())
    product_id=bs.find(id='productTitle').get_text()
    print(product_id.strip())
    price_id=bs.find(id="apex_desktop").get_text()
    #print(price_id.strip())
    price=price_id[15:20]
    print(price)
    price_float=float(price.replace(",",""))


    #print(price_float)

    file_exists = True
    if not os.path.exists("./price.csv"):
            file_exists= False
    with open("price.csv","a" ) as flie:
        writer = csv.writer(flie,lineterminator='\n')
        fiedls = ["Timestamp","Price(INR)"]
        if not file_exists:
           writer.writerow(fiedls)
        timestamp=f"{datetime.datetime.date(datetime.datetime.now())}, {datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp,price_float])
        print("worte data to file")
        return price_float

def send_email():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hk3143774@gmail.com','fdnamflrorimtrpd')

    subject="Hey the price has fell down.I hope u get it now"
    body="Go order now before the price increases\n link is here:https://www.amazon.in/dp/B0BSNQ2KXF/?_encoding=UTF8&ie=UTF8&ref_=hero1_OP11R&pf_rd_r=B9AXNCRD8T0QNHWE703P&pf_rd_p=05883749-7a3a-4b96-a8ea-8870f94c44b3&pd_rd_r=b167fa79-237d-41c1-a284-060e762442d6&pd_rd_w=UYjRe&pd_rd_wg=GzW7y "
    msg = f"Subject: {subject}\n\n\n{body}"
    server.sendmail('grohithreddy88@gmail.com','hk3143774@gmail.com',msg)
    print("email sent")
    server.quit()
while True:
    Price = check_our_price()
    if(Price < 3000):
        send_email()
        break

