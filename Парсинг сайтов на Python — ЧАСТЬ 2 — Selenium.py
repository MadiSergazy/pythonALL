# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/results?search_query={}'.format(str(video))

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element(By.ID, "video-title").click()

'''
from selenium import webdriver

##селениюм позволит автоматизировать
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.youtube.com/")  #

# element = browser.find_element(By.XPATH, """//*[@id="details"]""") #нажатие на видео
# element.click()

element = browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button")
browser.implicitly_wait(2)
seatrchBar = browser.find_element(By.ID, "search")

browser.implicitly_wait(2)
seatrchBar.send_keys("LLL")
browser.implicitly_wait(2)






#про регистрайцию
# seatrchBar = browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button")
# seatrchBar.click()




# element.click()#нажимаем на кнопку
#
# nomerSend = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
# nomerSend.send_keys("saitamenter@gmail.com")#
#
# nomerSend = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
# nomerSend.click()#нажимаем на кнопку далее
'''



