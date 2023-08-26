import requests
import csv
from bs4 import BeautifulSoup

# will use lxml as the parser for beatifulsoup

season= input('Please input a season in the form season-YYYY: ')
page =requests.get(f"https://www.anime-planet.com/anime/seasons/{season}")

def main(page):
    src=page.content
    soup=BeautifulSoup(src,"lxml")

    site_container=soup.find("div",id="siteContainer")

    def get_anime_info(site_container):
        season_name=site_container.find("h1").text.strip()
        #The first container is the anime container, and the rest of the containers could be found through extracting h4 titles
        animetypes=['Series']
        temp=site_container.find_all("h4")
        temp = [tag.text.strip() for tag in temp]
        animetypes+=temp
        anime_containers=site_container.find_all("ul",{'class':'cardDeck'})
        print(anime_containers)
        #The number of the containers should match the number of anime types

    get_anime_info(site_container)

main(page)
