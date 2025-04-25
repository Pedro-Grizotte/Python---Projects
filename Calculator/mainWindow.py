import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Confiração do Layout
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Título do projeto
        self.setWindowTitle('Calculadora')  
    
    def adjustFixedSize(self):
        # Ajuste da janela
        self.adjustSize()
        self.setFixedSize(self.width(), self.height()) 