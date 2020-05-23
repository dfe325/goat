from selenium import webdriver
#import chromedriver_binary

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
