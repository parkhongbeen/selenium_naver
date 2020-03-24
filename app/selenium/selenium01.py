from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
url = 'https://google.com'
driver.get(url)