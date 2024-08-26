import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt Image, Text, and Button Example')
        self.setGeometry(100, 100, 800, 800)

        # 创建中心Widget和布局
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 上半部分：图片显示
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(800, 600)  # 设置图片显示区域的大小
        self.image_label.setAlignment(Qt.AlignCenter)
        self.load_image('output/detected.jpg')  # 加载初始图片

        # 中部：文本输出域
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.load_text('output/displayOutput.txt')  # 加载初始文本

        # 下半部分：按钮
        self.button = QPushButton('Refresh Image and Text', self)
        self.button.clicked.connect(self.refresh_image_and_text)

        layout.addWidget(self.image_label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    def load_text(self, text_file_path):
        with open(text_file_path, 'r') as file:
            self.text_edit.setText(file.read())

    def refresh_image_and_text(self):
        # 执行外部Python脚本
        subprocess.run(['python', 'detect.py'], check=True)

        # 刷新图片
        self.load_image('output/detected.jpg')  # 假设外部脚本生成的图片保存在此路径

        # 刷新文本
        self.load_text('output/displayOutput.txt')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())