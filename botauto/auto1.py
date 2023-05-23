import os
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By


url = "http://65.186.78.52/MUSIC/ORIG/T/Top%20Hits/1986/"
driver = webdriver.Chrome() # hoặc sử dụng trình duyệt khác
driver.get(url)

links = driver.find_elements(By.XPATH, "a")
for link in links:
    href = link.get_attribute("href")
    if href.endswith(".mp3"):
        file_name = link.text + ".mp3"
        folder_path = "C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "wb") as f:
            f.write(requests.get(href).content)