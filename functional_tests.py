from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8196')

assert 'Django' in browser.title
