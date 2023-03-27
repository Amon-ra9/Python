import pyttsx3              #Import module for text-to-speech synthesis
engine = pyttsx3.init()     #create variable engine and load and use pyttxt3 module
voices = engine.getProperty('voices')       #access properties of engine
engine.setProperty('rate', 165)             #rate of speed
engine.setProperty('voice', voices[1].id)   #use voice 1, female (0 = male)

from bs4 import BeautifulSoup   #import BeautifulSoup Library (scraping tool) (installed in pycharm terminal with pip install bs4)
import requests                 #import the request library (installed in the pycharm terminal with pip install requests)

website = 'https://subslikescript.com/movie/Titanic-120338' #creat a variable titles website and define the value
result = requests.get(website)  #create a variable title result and get the information from the website variable
content = result.text           #create a variable title content and pass the text to the variable

soup = BeautifulSoup(content, 'lxml')   #create variable titled soup and use BeautifulSoup to scrape the content using the lxml parser (html code)
print(soup.prettify())  #make the text look presentable

box = soup.find('article', class_= 'main-article') #find main article section of html page, find a class named main-srticle

title = box.find('h1').get_text() #find h1, get the text and place it in title variable

transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ') #find div section of html page, find a class named full-script
print(title)        #testing retrieval of title text
print(transcript)   #testing retrieval of transcript text

engine.say(title)   #passing title test to voice engine
engine.runAndWait() #run and wait

engine.say(transcript)  #passing transcript text to voice engine
engine.runAndWait()     #run and wait


