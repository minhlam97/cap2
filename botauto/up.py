from selenium import webdriver


url = 'http://127.0.0.1:8000/admin/api/song/add/'
filename = 'path/to/your/file.mp3'

driver = webdriver.Chrome()
driver.get(url)

username = "admin"
password = "admin"

username_input = driver.find_element_by_css_selector('input[name="username"]')
username_input.send_keys(username)
password_input = driver.find_element_by_css_selector('input[name="password"]')
password_input.send_keys(password)
login_button = driver.find_element_by_css_selector('button[type="submit"]')
login_button.click()


mp3 = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="id_mp3_file"]'))).click()


