from bs4 import BeautifulSoup
import requests


class NewsScraper:
    def scrapenews(self, url, tag):
        response = requests.get(url + '/'+ tag)
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        news = soup.find_all('article', class_='article-image')
        # print(news)

        i = 0

        newsList = []

        for article in news:
            newsitem= {
                'link': "https://kathmandupost.com"+article.find('a').get('href'),
                'title': article.find('h3').text,
                'author': article.find('span', class_='article-author').find('a').text,
                'description': article.find('p').text,
                'image': article.find('img', class_="img-responsive")['data-src'] 
            }

            newsList.append(newsitem)

            # title = 
            # author = 
            # description = 
            # image = 
            # print(image)
            i = i+1
            if(i>5):
             break
        # print(newsList)
        return newsList
        
      

NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'national')
NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'valley')
NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'art-culture')
NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'money')
NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'sports')


