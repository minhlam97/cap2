from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'http://127.0.0.1:8000/admin/api/song/add/'
# filename = 'path/to/your/file.mp3'

driver = webdriver.Chrome()
driver.get(url)

username = "admin"
password = "admin"

username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_input.send_keys(username)
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_input.send_keys(password)
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(5)


name = driver.find_element(By.NAME, 'name').send_keys("admmin")
    
driver.find_element(By.ID, "id_poster").send_keys()
    # ("C:\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele")
    # poster = driver.find_element(By.XPATH, '//*[@id="id_poster"]').click()
time.sleep(5)
# poster_up = ("C:\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\adele").send_keys()
    # poster=driver.find_element(By.XPATH, '//*[@id="id_poster"]').click()
    # name1 = "Adele"
    # name = driver.find_element(By.XPATH, '//*[@id="id_name"]').send_keys(name1)

    # mp3_file=driver.find_element(By.XPATH, '//*[@id="id_mp3_file"]')

    # mp3 = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_mp3_file"]'))).click()


