import requests
import csv
from bs4 import BeautifulSoup

# will use lxml as the parser for beatifulsoup

season= input('Please input a season in the form season-YYYY: ')
if not season:
    season = 'summer-2023'
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
        #The number of the containers should match the number of anime types
        for typ,container in zip(animetypes,anime_containers):
            animes=container.find_all("li") # All animes for a specific type
            print(f'#------------------------{typ}----------------------------#')
            for anime in animes:
                number_of_episodes=anime.attrs['data-total-episodes']
                if typ=='Series':
                    title=anime.text.strip()[3:]  
                else:
                    title=anime.text.strip()
                title=title.replace("Add to list", "").strip()
                print(title)
                print('...............................................')
            

    get_anime_info(site_container)

main(page)
