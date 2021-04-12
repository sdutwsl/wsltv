#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import bs4
import json

list_page=requests.get("http://share.dmhy.org/",proxies={"http":"http://localhost:1080"})

main_bs=bs4.BeautifulSoup(list_page.content,"html.parser")
main_table=main_bs.find("table",{"class":"tablesorter"})

trs=main_table.findAll("tr")

s=""

for tr in trs:
    td_title=tr.find("td",{"class":"title"})
    if td_title is not None:
        maga=tr.find("a",{"class":"download-arrow arrow-magnet"})
        s+="🆒"+"".join(td_title.text.split())+"🆒\n"
        s+="🌧"+maga["href"]+"🌧\n"
f=open("tele/bitconn.txt","wb")
f.write(s.encode('utf-8'))
f.close()