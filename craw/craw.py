import requests
import bs4

list_page=requests.get("http://share.dmhy.org/",proxies={"http":"http://localhost:8889"})

main_bs=bs4.BeautifulSoup(list_page.content,"html.parser")
main_table=main_bs.find("table",{"class":"tablesorter"})

trs=main_table.findAll("tr")

for tr in trs:
    tds=tr.findAll("td")
    print(tds)