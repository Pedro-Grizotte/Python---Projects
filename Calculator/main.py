import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    label = QLabel('Texto teste')
    label.setStyleSheet(
        'font-size: 150px;'
    )
    window.v_layout.addWidget(label)
    window.adjustFixedSize()
    window.show()
    app.exec()