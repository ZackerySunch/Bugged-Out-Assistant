import time
import random
import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
import cv2

class OpenVideo:
    def __init__(self, video_folder):
        self.video_folder = video_folder
        self.root = None
        self.label = None
        self.cap = None
        self.imgtk = None

    # 🔥 動態檔案路徑修正 (支援 .exe 打包)
    def get_resource_path(self, relative_path):
        if getattr(sys, '_MEIPASS', None):  # PyInstaller 打包時的路徑
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def getvideo(self):
        # 檢查資料夾是否存在
        if not os.path.exists(self.video_folder):
            print("❌ 資料夾不存在:", self.video_folder)
            return
        
        # 隨機選擇影片
        video_files = [f for f in os.listdir(self.video_folder) if f.endswith('.mp4')]
        if not video_files:
            print("❌ 找不到影片檔案")
            return

        random_video = random.choice(video_files)
        video_path = self.get_resource_path(os.path.join(self.video_folder, random_video))

        # 開啟影片
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            print(f"❌ 無法讀取影片檔案: {video_path}")
            return
        
        # 建立 Tkinter 視窗
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        
        self.label = tk.Label(self.root)
        self.label.pack(fill=tk.BOTH, expand=True)
        
        start_time = time.time()

        def show_frame():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                self.imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = self.imgtk
                self.label.configure(image=self.imgtk)
            if time.time() - start_time < 5:
                self.label.after(10, show_frame)
            else:
                self.cap.release()
                self.root.destroy()
        
        show_frame()
        self.root.mainloop()

if __name__ == '__main__':
    video_folder = '影片'  # 影片資料夾名稱

    # 🔥 確保 PyInstaller 打包後路徑正確
    if getattr(sys, '_MEIPASS', None):
        video_folder = os.path.join(sys._MEIPASS, '影片')

    if not os.path.exists(video_folder):
        print("❌ 資料夾不存在:", video_folder)
    else:
        video_open = OpenVideo(video_folder)
        video_open.getvideo()
