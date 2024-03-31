import requests
from bs4 import BeautifulSoup
import csv

date=input('please enter date with format:MM/dd/yy:')
page=requests.get(f"https://www.yallakora.com/match-center/? date={date}")

def main(page):
    src=page.content 
    soup=BeautifulSoup(src,'lxml')
    
    matches_details=[]

    championships=soup.find_all('div',{'class':'matchCard'})
    

    def get_match_info(championships):
        championship_title=championships.contents[1].find('h2').text.strip()
        print(championship_title)
    get_match_info(championships[0])
    
main(page)