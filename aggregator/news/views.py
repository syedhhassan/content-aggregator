from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

def news(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    new = soup.find_all('h3')
    news = []
    for i in new:
        news.append(i.text)
    return news

# Create your views here.
    
def sports(request):
    url = "https://www.nytimes.com/section/sports"
    received_news = news(url)    
    return render(request, 'index.html', {"news": received_news} )