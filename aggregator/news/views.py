from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

# Create your views here.
#def news(url):
sports_req = requests.get("https://www.nytimes.com/section/sports")
sports_soup = BeautifulSoup(sports_req.content, 'html.parser')
sports_new = sports_soup.find_all('h3')
sports_img = sports_soup.find_all('img')
sports_news = []
sports_images = []
for i in sports_new:
    sports_news.append(i.text)
for j in sports_img:
    sports_images.append(j.content)
    
def sports(request):
    return render(request, 'index.html', {"sports_images": sports_images, "sports_news": sports_news} )