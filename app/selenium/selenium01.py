from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
url = 'https://google.com'
driver.get(url)

# 검색창이 갖고 있는 클래스로 접근하고 파이썬을 검색
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
# 검색 후 나온 결과중에서 클래스로 접근해 엔터치도록 명령
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
# 검색 후 나온 결과중에서 list의 2번째를 클릭하도록 명령 / 이때, 주의할 점은 복수인지 단수인지 잘 봐야
driver.find_elements_by_css_selector('.LC20lb')[1].click()
