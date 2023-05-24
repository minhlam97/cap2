from selenium import webdriver
from mutagen.mp3 import MP3
import os

# driver = webdriver.Chrome()
folder_path = 'C:\\Users\\OS\\OneDrive\\Máy tính\\CAP2\\lam\\Songs\\Adele'
file_list = os.listdir(folder_path)

for file_name in file_list:
    # Kiểm tra tệp có phải là tệp âm thanh (ví dụ: mp3) hay không
    if file_name.endswith('.mp3'):
        # Xây dựng đường dẫn đầy đủ đến tệp âm thanh
        file_path = os.path.join(folder_path, file_name)
        
        # Mở tệp âm thanh và trích xuất thông tin
        audio = MP3(file_path)
        
        # Trích xuất thông tin bài hát
        song_title = audio['title'][0]
        artist = audio['artist'][0]
        duration = audio.info.length
        
        # In ra thông tin bài hát
        print("Tên bài hát:", song_title)
        print("Ca sĩ:", artist)
        print("Thời gian:", duration)