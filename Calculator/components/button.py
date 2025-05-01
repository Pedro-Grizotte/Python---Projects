from PySide6.QtWidgets import QPushButton, QGridLayout
from variable import FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from PySide6.QtCore import Slot

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from display import Display
    from mainWindow import Info

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        font = self.font()
        font.setPixelSize(FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self._equation = ''
        self._initialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._initialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)
    
    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertButtonText, button)
                self._connectButtonClicked(button, slot)
    
    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
    
    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)
    
        if text in '+-/*':
            self._connectButtonClicked(button, self._makeSlot(
                self._operatorClicked, button)
            ) 

        if text in '=':
            self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot
    
    def _insertButtonText(self, button):
        button_text = button.text()
        newDisplayValue = self.display.text() + button_text
        if not isValidNumber(newDisplayValue):
            return 

        self.display.insert(button_text)
    
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._initialValue
        self.display.clear()
    
    def _operatorClicked(self, button):
        buttonText = button.text() # +-/* Recebe o texto do operador
        displayText = self.display.text() # Recebe o numero da esquerda
        self.display.clear() # Limpa o display

        if not isValidNumber(displayText) and self._left is None:
            # Se caso a pessoa não digite numeros antes 
            # de clicar no operador, a calculadora
            # não executa nada
            return
    
        if self._left is None:
            self._left = float(displayText)
        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'
    
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            # Se não houver nada na direita 
            # O botão de '=' não realiza a conta
            return
        
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 0.0
        try:
            result = eval(self.equation)
        except ZeroDivisionError:
            print('Divisão por zero!')
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None

