import requests
from bs4 import BeautifulSoup
import nltk.corpus
import re
import matplotlib.pyplot as plt

url = 'https://www.ft.com/'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

titles = soup.find_all(class_='o-teaser__heading')
strTitle = str(titles)

cleanTitle = re.sub('<[^<]+?>', '', strTitle)
cleanedTitleA = cleanTitle.replace(',', '')
cleanedTitleB = cleanedTitleA.replace('’', '')
cleanedTitleC = cleanedTitleB.replace(':', '')
cleanedTitleD = cleanedTitleC.replace('‘', '')

# print(cleanedTitleD)
tokens = nltk.word_tokenize(cleanedTitleD)
print(tokens)
fd = nltk.FreqDist(tokens)
fd.plot(30, cumulative = False)

tagged = nltk.pos_tag(tokens)
people = nltk.chunk.ne_chunk(tagged)
print(people)
