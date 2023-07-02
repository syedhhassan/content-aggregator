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

def home(request):
    url = "https://www.nytimes.com/"
    received_news = news(url)
    json = {"name": "International", "news": received_news}
    return render(request, 'index.html', json)

def science(request):
    url = "https://www.nytimes.com/section/science"
    received_news = news(url)    
    json = {"name": "Science", "news": received_news}
    return render(request, 'index.html', json)

def health(request):
    url = "https://www.nytimes.com/section/health"
    received_news = news(url)
    json = {"name": "Health", "news": received_news}
    return render(request, 'index.html', json)

def technology(request):
    url = "https://www.nytimes.com/section/technology"
    received_news = news(url)    
    json = {"name": "Technology", "news": received_news}
    return render(request, 'index.html', json)

def sports(request):
    url = "https://www.nytimes.com/section/sports"
    received_news = news(url)
    json = {"name": "Sports", "news": received_news}
    return render(request, 'index.html', json)

def education(request):
    url = "https://www.nytimes.com/section/education"
    received_news = news(url)
    json = {"name": "Education", "news": received_news}
    return render(request, 'index.html', json)

def business(request):
    url = "https://www.nytimes.com/section/business"
    received_news = news(url)
    json = {"name": "Business", "news": received_news}
    return render(request, 'index.html', json)
