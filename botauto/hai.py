from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://houseviet.vn/nha-dat-ban")

sessions = driver.find_elements_by_class_name("property-item")

# In ra số lượng session có class="property-item" được chọn
print("Số lượng session có class=\"property-item\": ", len(sessions))

# Đóng trình duyệt
driver.quit()


