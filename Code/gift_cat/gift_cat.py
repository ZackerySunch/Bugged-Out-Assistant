import tkinter as tk
import pyautogui
import time
import pygame
from PIL import Image, ImageTk

class MovingWindow:
    def __init__(self):
        # 初始化 pygame 播放音樂
        pygame.mixer.init()

        # 播放音樂
        self.play_music("catmeo.mp3")  # 請將 'your_music_file.mp3' 換成你的 MP3 文件路徑

        # 初始化 Tkinter 視窗
        self.window = tk.Tk()
        self.window.title("移動視窗")
        self.window.geometry("400x200")  # 視窗大小
        self.window.configure(bg="lightblue")  # 背景顏色
        self.window.overrideredirect(True)  # 設置無邊框視窗

        # 載入圖片並調整大小填滿視窗
        self.image = Image.open("catUI.jpg")  # 替換為你的圖片路徑
        self.image = self.image.resize((400, 200))  # 調整圖片大小填滿視窗
        self.image_tk = ImageTk.PhotoImage(self.image)

        # 顯示圖片
        self.img_label = tk.Label(self.window, image=self.image_tk)
        self.img_label.place(relx=0.5, rely=0.5, anchor="center")  # 使圖片居中顯示

        # 顯示一些內容
        label = tk.Label(self.window, text="從右下角移動到螢幕可視範圍內", bg="lightblue", font=("Arial", 16), fg="white")
        label.pack(pady=80)

    def play_music(self, music_file):
        """播放 MP3 音樂"""
        try:
            pygame.mixer.music.load(music_file)  # 載入音樂檔案
            pygame.mixer.music.play(-1)  # -1 表示循環播放
        except Exception as e:
            print(f"無法播放音樂檔案: {e}")

    def move_window(self):
        # 獲取螢幕的解析度
        screen_width, screen_height = pyautogui.size()

        # 設定視窗的初始位置為螢幕右下角
        initial_x = screen_width - 1  # 右邊邊緣
        initial_y = screen_height - 1  # 底部邊緣

        # 設定視窗的目標位置（可視範圍內）
        target_x = screen_width - 420  # 讓視窗完全顯示
        target_y = screen_height - 220-30  # 讓視窗完全顯示

        # 設定初始位置
        self.window.geometry(f"+{initial_x}+{initial_y}")
        
        # 顯示視窗，並等待 1 秒鐘
        self.window.after(1000, self.animate_window, initial_x, initial_y, target_x, target_y)

    def animate_window(self, start_x, start_y, end_x, end_y):
        # 逐漸將視窗移動到目標位置
        steps = 30  # 移動的步驟數
        for i in range(steps):
            new_x = start_x - (start_x - end_x) * (i / steps)
            new_y = start_y - (start_y - end_y) * (i / steps)
            self.window.geometry(f"+{int(new_x)}+{int(new_y)}")
            time.sleep(0.03)  # 每次移動的延遲時間，製造動畫效果
            self.window.update()

if __name__ == "__main__":
    app = MovingWindow()
    app.move_window()  # 開始移動視窗
    app.window.mainloop()  # 啟動 Tkinter 事件循環
