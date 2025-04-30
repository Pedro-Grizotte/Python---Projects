import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variable import ICON, setupStyle
from pathlib import Path
from display import Display
from mainWindow import MainWindow, Info

PARENT = Path(__file__).parent
COMPONENTS = PARENT / 'components'
ARQUIVES = COMPONENTS / 'button.py'
sys.path.insert(0, ARQUIVES)

from components.button import Button, ButtonsGrid

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupStyle(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(ICON))
    app.setWindowIcon(icon)

    # Info - Caso queira ter um historico da calculadora
    # info = Info('2.0 ^ 10.0 = 1024')
    # window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo') # Placeholder
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.vLayout.addLayout(buttonsGrid)

    # Executa o programa
    window.adjustFixedSize()
    window.show()
    app.exec() 