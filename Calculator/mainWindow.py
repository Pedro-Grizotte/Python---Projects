import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Confiração do Layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título do projeto
        self.setWindowTitle('Calculadora')  
    
    def adjustFixedSize(self):
        # Ajuste da janela
        self.adjustSize()
        self.setFixedSize(self.width(), self.height()) 
    
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
