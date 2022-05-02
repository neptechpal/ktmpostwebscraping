from fastapi import FastAPI
from scraper import NewsScraper

app= FastAPI()

@app.get("/national")
async def getpoliticsnews():

    return NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com", 'national')


@app.get("/valley")
async def getvalleynews():

    return NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com", 'valley')


@app.get("/art-culture")
async def getart_culturenews():

    return NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com", 'art-culture')


@app.get("/money")
async def getmoneynews():

    return NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com", 'money')



@app.get("/sports")
async def getsportsnews():

    return NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com", 'sports')








# NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'national')
# NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'valley')
# NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'art-culture')
# NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'money')
# NewsScraper.scrapenews(NewsScraper, "https://kathmandupost.com/national", 'sports')