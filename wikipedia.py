from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Edge()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#przechodzi do div ' articlecount' i pobiera tresc znacznika 'a'
articles = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
talk_button = driver.find_element(By.ID,'pt-anontalk')
print(talk_button.text)
#talk_button.click() # klika w element :)
#print(articles.text)

#szuka linku z podanym tekstem
all_portals= driver.find_element(By.LINK_TEXT,'MediaWiki') 
#all_portals.click()
#wslazuje na wyszukiwarke
search_bar = driver.find_element(By.NAME,'search')
#wpisuje w wyszukiwarke co chcemy
search_bar.send_keys('Eden Hazard')
#wysylamy ENTER w celu zatwierdzenia wyszukiwania
search_bar.send_keys(Keys.ENTER)
#wybiera pierwszy artykul z listy
first_article = driver.find_element(By.CSS_SELECTOR,'.mw-search-result-heading a')
print(first_article.text)
first_article.click()
