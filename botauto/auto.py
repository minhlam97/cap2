from selenium import webdriver
import selenium.webdriver as webdriver
import requests
import os

url = "https://dl3.parsiane.ir/music/a/adele/"
driver = webdriver.Chrome()
driver.get(url)

mp3_links = driver.find_elements_by_xpath('//a[contains(@href, ".mp3")]')

if not os.path.exists("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\Songs\\adele"):
    os.makedirs("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\Songs\\adele")

for link in mp3_links:
    url = link.get_attribute("href")
    response = requests.get(url)
    filename = url.split("/")[-1]
    filepath = os.path.join("C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\Songs\\adele", filename)
    with open(filepath, "wb") as f:
        f.write(response.content)

# Đóng trình duyệt
driver.quit()