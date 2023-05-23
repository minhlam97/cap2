from selenium import webdriver
import selenium.webdriver as webdriver
import requests
import os
from selenium.webdriver.common.by import By


# url = "https://dl3.parsiane.ir/music/a/adele/"
# url = "https://dl2.beelody.com/Free/2021/7/Anne-Marie%20-%20Therapy%20%282021%29%20%5BBeelody%5D/" #freelink
# url = "https://freepd.com/music/" #freelink100bai
url = "http://sv2.mybia2music.com/s2/Music/1391/6%20Shahrivar/9201/Adele%20-%20Greatest%20Hits%20[128]/" 



driver = webdriver.Chrome()
driver.get(url)

mp3_links = driver.find_elements(By.XPATH, '//a[contains(@href, ".mp3")]')
# mp3_links = driver.find_elements_by_xpath('//a[contains(@href, ".mp3")]')


if not os.path.exists("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele"):
    os.makedirs("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele")

for link in mp3_links:
    url = link.get_attribute("href")
    response = requests.get(url)
    filename = url.split("/")[-1]
    song_title = filename.replace("%20" ," ")
    filepath = os.path.join("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele", song_title)
    with open(filepath, "wb") as f:
        f.write(response.content)

driver.quit()