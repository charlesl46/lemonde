import requests
from bs4 import BeautifulSoup

class Article:
    """
    A class to modelize Le Monde newspaper articles
    """
    def __init__(self) -> None:
        pass

    def _set_title(self,title : str) -> None:
        self.title = title

    def _set_link(self,link : str) -> None:
        self.link = link

    def _set_image(self,image : str) -> None:
        self.image = image

    def _set_type(self,type : str) -> None:
        self.type = type

class LeMonde:
    """
    A class to modelize LeMonde articles
    """
    def __init__(self) -> None:
        pass

    def get_articles(self) -> list[Article]:
        articles = []
        response = requests.get("https://www.lemonde.fr/")
        soup = BeautifulSoup(response.text,"html.parser")
        for div in soup.findAll("div",{'class' : 'article'}):
            article = Article()
            title = div.select_one(".article__title")
            article._set_title(title.text)
            link = div.find('a')["href"]
            article._set_link(link)
            try:
                image = div.find("img")["src"]
            except:
                try:
                    image = div.find("img")["data-src"]
                except:
                    image = None
            article._set_image(image)
            try:
                type = div.select_one('.article__type').text
            except:
                type = None
            article._set_type(type)
            articles.append(article)
        return articles









