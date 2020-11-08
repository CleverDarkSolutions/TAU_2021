from selenium import webdriver
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

logger.info('Przechodzę na stronę Zalando')
driver.get('https://www.zalando.pl/')
temp = driver.find_element_by_class_name('z-navicat-header_navToolItemLink')
temp.click()
logger.warning('Jakieś ostrzeżenie')
temp = driver.find_element_by_id('login.email')
temp.send_keys("login")
logger.error('Jakiś Error')

driver.close()