import keyboard
import subprocess
import pyautogui
import time
import random  # 引入 random 模組

class AppLauncher:
    def __init__(self):
        self.running = True
        
        # 定義應用程式列表
        self.app_list = [
            "chrome",         # 'esc' 打開 Google Chrome
            "word",           # 'd' 打開 Word
            "powerpoint",     # 't' 打開 PowerPoint
            "cmd",            # 'm' 打開 C`MD
            "vscode",         # 'k' 打開 VSCode
            "steam",          # 'u' 打開 Steam
            "vul3nj04q06",    # 'i' 打開某應用程式 (這是示例名)
            "ji3ap7x96ru03t865k4ek72u04sl3u.3ao6u.3wk41u,62k7vm,6vu6y xul4"  # 'h' 打開某應用程式 (這是示例名)
        ]
        
        # 定義對應的快捷鍵
        self.key_actions = {
            "esc": self.open_random_app,   # 'esc' 隨機打開應用程式
            "d": self.open_random_app,     # 'd' 隨機打開應用程式
            "t": self.open_random_app,     # 't' 隨機打開應用程式
            "m": self.open_random_app,     # 'm' 隨機打開應用程式
            "k": self.open_random_app,     # 'k' 隨機打開應用程式
            "u": self.open_random_app,     # 'u' 隨機打開應用程式
            "i": self.open_random_app,     # 'i' 隨機打開應用程式
            "h": self.open_random_app      # 'h' 隨機打開應用程式
        }

    def open_random_app(self):
        """隨機選擇並開啟一個應用程式"""
        app_name = random.choice(self.app_list)  # 隨機選擇一個應用程式
        print(f"正在隨機打開應用程式: {app_name}")
        pyautogui.press("win")
        time.sleep(0.5)  # 等待搜尋框出現
        pyautogui.write(app_name, interval=0.1)
        time.sleep(0.5)  # 等待搜尋框出現
        pyautogui.press("enter")

    def exit_program(self):
        """結束程式"""
        print("程式結束！")
        self.running = False

    def monitor_keys(self):
        """監控鍵盤輸入"""
        while self.running:
            for key, action in self.key_actions.items():
                if keyboard.is_pressed(key):
                    action()

if __name__ == "__main__":
    app = AppLauncher()  # 創建 AppLauncher 類別的實例
    app.monitor_keys()  # 啟動鍵盤監聽

