import os
import sys
import time
import psutil
import subprocess
import webbrowser
from PIL import Image, ImageTk
from PyQt6 import QtWidgets, QtGui, QtCore
from pynput.keyboard import Controller,Listener,Key
from PyQt6.QtWidgets import QMessageBox,QStackedLayout

class Check_Start(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('請確認是否執行')
        self.setFixedSize(600, 400)
        self.move(100, 100)
        self.setStyleSheet("background-color: black;")
        
        self.label = QtWidgets.QLabel('桌面智能(障)助理', self)
        self.label.setFont(QtGui.QFont('Microsoft JhengHei', 40))
        self.label.setStyleSheet("color: white;")
        self.label.setGeometry(80, 100, 440, 50)
        
        self.check_button = QtWidgets.QPushButton('確認', self)
        self.check_button.setFont(QtGui.QFont('Microsoft JhengHei', 20))
        self.check_button.setStyleSheet("color: white; background-color: #333333;")
        self.check_button.setGeometry(180, 200, 240, 60)
        self.check_button.clicked.connect(self.on_check_button_click)
        
        self.animations = []
        self.animations.append(self.fade_in_animation(self.label))
        self.animations.append(self.fade_in_animation(self.check_button))
        
        self.show()
        

        
    def fade_in_animation(self, widget):
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(1250)
        animation.setStartValue(0)
        animation.start()
        return animation
        animation.start()
        
    def on_check_button_click(self):
        QMessageBox.information(self, "訊息", "確認執行 第一次")
        QMessageBox.information(self, "訊息", "確認執行 第二次")
        QMessageBox.information(self, "訊息", "確認執行 第三次")
        self.close()
        
        self.blue_window = QtWidgets.QWidget()
        self.blue_window.showFullScreen()
        
        try:
            # 確保路徑正確
            image_path = os.path.join(os.path.dirname(__file__), "448vc-y35ua.png")
            
            if not os.path.exists(image_path):
                raise FileNotFoundError("圖片文件不存在")

            # 使用 QPixmap 直接載入圖片（更穩定）
            pixmap = QtGui.QPixmap(image_path)

            if pixmap.isNull():
                raise Exception("圖片加載失敗")

            # 建立 QLabel 並顯示圖片
            self.image_label = QtWidgets.QLabel(self.blue_window)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
            # 使用 QVBoxLayout 確保佈局不出錯
            layout = QtWidgets.QVBoxLayout(self.blue_window)
            layout.addWidget(self.image_label)
            self.blue_window.setLayout(layout)

            print("✅ 圖片加載成功")
        except Exception as e:
            print(f"❌ 圖片加載失敗: {e}")
            return

        
        QtCore.QTimer.singleShot(5000, self.close_window)
        
    def close_window(self):
        try:
            self.blue_window.close()
            self.main_window = Main()
        except:
            pass
        
class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.animations = []
        self.initUI()
        
    def initUI(self):
        print("mainwindow")
        self.setWindowTitle('桌面智能(障)助理')
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        
        layout = QtWidgets.QVBoxLayout()
        
        self.label = QtWidgets.QLabel('電腦性能測試', self)
        self.label.setFont(QtGui.QFont('Microsoft JhengHei', 40))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.start_button = QtWidgets.QPushButton('開始測試(小小的測試)', self)
        self.start_button.setFont(QtGui.QFont('Microsoft JhengHei', 20))
        self.start_button.setStyleSheet("color: white; background-color: #333333;")
        self.start_button.clicked.connect(self.start_button_clicked)
        layout.addWidget(self.start_button)
        
        self.animations.append(self.fade_in_animation(self.label))
        self.animations.append(self.fade_in_animation(self.start_button))
        
        self.setLayout(layout)
        
        self.left_word()
        
        self.show()
    
    def start_button_clicked(self):
        self.fade_out_animation(self.label)
        self.fade_out_animation(self.start_button)
        QtCore.QTimer.singleShot(1250, self.open_browser)
        
    def open_browser(self):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        for i in range(5):
            for i in range(5):
                webbrowser.open(url)  # 指定要開啟的網頁 URL
            time.sleep(2)
        webbrowser.open(url)
        time.sleep(5)  # 等待三秒
        os.system("taskkill /im chrome.exe /f")  # 關閉 Chrome 瀏覽器
        self.destroy()
        start = StartBreak()
        
    def left_word(self):
        print("left_word")
        ram_info = psutil.virtual_memory()
        ram_total = ram_info.total // (1024 ** 3)
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        
        labels = [
            f'CPU 核心數量: {cpu_cores} (你沒有64核心ㄟ~ 可能不夠喔)',
            f'CPU 執行緒數量: {cpu_threads} (你沒有128執行續 真窮ㄟ)',
            f'RAM: {ram_total} GB (好可憐 只有{ram_total}GB 我曾祖父的都比你多)',
            'GPU:不是NVIDIA H300 一律省略 (就算有5090也不行)'
        ]
        
        y_positions = [325, 400, 475, 550]
        
        for label_text, y in zip(labels, y_positions):
            label = QtWidgets.QLabel(label_text, self)
            label.setFont(QtGui.QFont('Microsoft JhengHei', 20))  # Adjusted font size to fit the screen
            label.setStyleSheet("color: white;")
            label.setGeometry(80, y, 1200, 50)
            label.setWordWrap(True)  # Enable word wrap to handle long text
            self.layout().addWidget(label)  # Add label to the layout
            self.animations.append(self.fade_in_animation(label))
            
    def fade_in_animation(self, widget):
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(1250)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.start()
        return animation
    
    def fade_out_animation(self, widget):
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(1250)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.start()
        return animation
      
class StartBreak(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.keybord = 0
        self.mouse = 0
        self.gift = 0
        self.software = 0 
        
        self.setWindowTitle('選擇功能')
        self.setFixedSize(800, 600)
        self.move(100, 100)
        self.setStyleSheet("background-color: black;")
        
        self.label = QtWidgets.QLabel('請選擇功能\n按一下啟用 按兩下還是啟用', self)
        self.label.setFont(QtGui.QFont('Microsoft JhengHei', 30))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(0, 15, 800, 100)
        
        buttons = [
            ('超現實輔助鍵盤', self.function1),
            ('鼠標智能走位器', self.function2),
            ('驚喜大禮包', self.function3),
            ('軟體智能啟動器', self.function4),
            ('開始', self.function5)
        ]
        
        y_positions = [150, 230, 310, 390, 470]
        
        self.animations = []
        self.animations.append(self.fade_in_animation(self.label))
        
        for (text, func), y in zip(buttons, y_positions):
            button = QtWidgets.QPushButton(text, self)
            button.setFont(QtGui.QFont('Microsoft JhengHei', 20))
            button.setStyleSheet("color: white; background-color: #333333;")
            button.setGeometry(300, y, 200, 60)
            button.clicked.connect(func)
            self.animations.append(self.fade_in_animation(button))
            
        
        self.show()
        
    def fade_in_animation(self, widget):
        effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QtCore.QPropertyAnimation(effect, b"opacity")
        animation.setDuration(1250)
        animation.setStartValue(0)
        animation.start()
        return animation
    
    def function1(self):
        QMessageBox.information(self, "訊息", "超現實輔助鍵盤 被選擇")
        self.keybord += 1

    def function2(self):
        QMessageBox.information(self, "訊息", "鼠標智能走位器 被選擇")
        self.mouse += 1

    def function3(self):
        QMessageBox.information(self, "訊息", "驚喜大禮包 被選擇")
        self.gift += 1
    
    def function4(self):
        QMessageBox.information(self, "訊息", "軟體智能啟動器 被選擇")
        self.software += 1
    
    def function5(self):
        QMessageBox.warning(self, "警告", "一旦啟動將無法關閉")
        self.close()
        
        processes = []
        
        if self.keybord == 1:
            print("keybord")
            file_path = "keybord.exe"
            processes.append(subprocess.Popen(file_path))
            
        if self.mouse == 1:
            print("mouse")
            file_path = "mouse\mouse.exe"
            processes.append(subprocess.Popen(file_path))
            
        if self.software == 1:
            print("software")
            file_path = "software.exe"
            processes.append(subprocess.Popen(file_path))
            
        if self.gift == 1:
            print("gift")
            file_path = "gift\gift.exe"
            processes.append(subprocess.Popen(file_path))
        
            # file_path1 = "gift_cat\gift_cat.exe"
            # processes.append(subprocess.Popen(file_path1))
        
        # Keep the main application running to allow VSCode to interrupt
        for process in processes:
            process.wait()

   
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    check_start = Check_Start()
    sys.exit(app.exec())
    
