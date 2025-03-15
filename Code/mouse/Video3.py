import cv2
import tkinter as tk
import pygame  # 用來播放音樂
from PIL import Image, ImageTk

# 播放視頻和音樂
def play_video():
    # 設定影片和音樂檔案路徑
    video_filename = "catKiss1.mp4"  # 確保影片檔案存在
    audio_filename = "catMeow.mp3"  # 確保 MP3 音檔存在

    cap = cv2.VideoCapture(video_filename)

    # 初始化 pygame 音樂播放器
    pygame.mixer.init()
    pygame.mixer.music.load(audio_filename)
    pygame.mixer.music.play()  # 開始播放音樂

    # 創建 tkinter 視窗並移除邊框
    window = tk.Tk()
    window.title("MP4 Video Player")
    window.overrideredirect(True)  # 移除視窗邊框
    window.attributes('-topmost', 1)  # 設定視窗為最上層

    # 設置視窗大小
    window_width = 1280
    window_height = 720

    # 獲取螢幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 計算視窗放置位置，使其顯示在螢幕中間
    x_pos = (screen_width // 2) - (window_width // 2)
    y_pos = (screen_height // 2) - (window_height // 2)

    # 設定視窗的位置和大小
    window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

    # 創建 Label 用於顯示視頻幀
    label = tk.Label(window)
    label.pack(fill=tk.BOTH, expand=True)  # 讓 Label 填滿整個視窗

    # 定義更新視頻幀的函數
    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame_resized = cv2.resize(frame, (window_width, window_height))
            frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

            # 創建圖像對象並更新 Label
            image = Image.fromarray(frame_resized)
            image_tk = ImageTk.PhotoImage(image=image)
            label.configure(image=image_tk)
            label.image = image_tk

            # 每 10 毫秒更新一次畫面
            label.after(10, update_frame)
        else:
            cap.release()  # 當視頻播放完畢，釋放資源
            pygame.mixer.music.stop()  # 停止播放音樂
            window.destroy()  # 關閉視窗
            window.quit()  # 確保 tkinter 事件迴圈結束
            
    # 開始播放視頻
    update_frame()

    # 啟動 tkinter 主循環
    window.mainloop()

# 設定主程式
if __name__ == "__main__":
    play_video()
