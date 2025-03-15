import math
import time
import random
import threading
import pyautogui
import cv2
import pygame
import tkinter as tk
from pynput import mouse
from PIL import Image, ImageTk

class MouseHeartMover:
    def __init__(self, center_x=800, center_y=400, size=30, steps=50, click_threshold=5, delay=0.1):
        self.mouse_controller = mouse.Controller()
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.steps = steps
        self.click_count = 0
        self.click_threshold = click_threshold
        self.delay = delay
        self.screen_width, self.screen_height = pyautogui.size()

        # 影片與音樂設定
        self.video_filename = "catKiss1.mp4"
        self.audio_filename = "catMeow.mp3"

    def heart_path(self, t):
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        return x * self.size + self.center_x, -y * self.size + self.center_y

    def move_mouse_in_heart(self):
        for i in range(self.steps + 1):
            t = (i / self.steps) * math.pi * 2
            x, y = self.heart_path(t)
            self.mouse_controller.position = (int(x), int(y))
            time.sleep(self.delay)

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            self.click_count += 1
            print(f"點擊次數: {self.click_count}")

            if self.click_count >= self.click_threshold:
                print("🎉 滑鼠開始畫愛心！")
                result = random.choice([1, 2, 3])

                if result == 1:
                    print("result=1")
                    self.move_mouse_in_heart()
                    threading.Thread(target=self.play_video, daemon=True).start()
                elif result == 2:
                    print("result=2")
                    self.move_mouse_randomly()
                elif result == 3:
                    print("result=3")
                    self.slow_move(self.screen_width - 30, 20)

                self.click_count = 0

    def play_video(self):
        """ 播放影片，並同步播放音效 """
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio_filename)
        pygame.mixer.music.play()

        cap = cv2.VideoCapture(self.video_filename)
        if not cap.isOpened():
            print("無法開啟影片")
            return

        # 使用 Tkinter 創建視窗
        window = tk.Tk()
        window.title("MP4 Video Player")
        window.overrideredirect(True)  # 去掉標題列
        window.attributes('-topmost', 1)

        # 設定視窗大小與位置
        window_width = 1280
        window_height = 720
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_pos = (screen_width // 2) - (window_width // 2)
        y_pos = (screen_height // 2) - (window_height // 2)
        window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

        label = tk.Label(window)
        label.pack(fill=tk.BOTH, expand=True)

        def update_frame():
            """ 顯示影片畫面 """
            ret, frame = cap.read()
            if ret:
                frame_resized = cv2.resize(frame, (window_width, window_height))
                frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame_resized)
                image_tk = ImageTk.PhotoImage(image=image)
                label.configure(image=image_tk)
                label.image = image_tk
                label.after(10, update_frame)
            else:
                cap.release()
                pygame.mixer.music.stop()
                window.destroy()

        update_frame()
        window.mainloop()

    def move_mouse_randomly(self, moves=10, interval=0.5):
        for _ in range(moves):
            x = random.randint(0, self.screen_width - 1)
            y = random.randint(0, self.screen_height - 1)
            self.mouse_controller.position = (x, y)
            time.sleep(interval)

    def slow_move(self, target_x, target_y, steps=100, duration=2):
        start_x, start_y = self.mouse_controller.position
        step_x = (target_x - start_x) / steps
        step_y = (target_y - start_y) / steps

        for i in range(steps):
            self.mouse_controller.position = (start_x + step_x * (i + 1), start_y + step_y * (i + 1))
            time.sleep(duration / steps)

    def start_listener(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()


if __name__ == "__main__":
    mover = MouseHeartMover(size=20, steps=50, delay=0.1)
    mover.start_listener()
