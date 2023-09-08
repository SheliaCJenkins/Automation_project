import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/Users/sheliajenkins/Desktop/chromedriver")

driver.get("http://www.youtube.com")

driver.implicitly_wait(5)


searchbox = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
searchbox.send_keys('baby dogs')

driver.implicitly_wait(3000)

searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
searchButton.click()

driver.implicitly_wait(3000)


video = driver.find_element_by_xpath("//*[@id='contents']/ytd-video-renderer[1]")
video.click()

ad = driver.find_element_by_xpath("//*[@id='skip-button:5']/span/button/span")
ad.click()

driver.implicitly_wait(10000)

time.sleep(30)

pause = driver.find_element_by_xpath("//*[@id='movie_player']/div[34]/div[2]/div[1]/button")
pause.click()



