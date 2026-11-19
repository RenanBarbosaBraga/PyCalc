import math
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import IsEmpty, IsNumOrDot, IsValidNumber, convertToNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: "Display", info: "Info", window: "MainWindow", *args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ["C", "◀", "^", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["", "0", ".", "="],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ""
        self._equationInitialValue = "Sua conta"
        self._left = None
        self._right = None
        self._operator = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for rowNumber, row in enumerate(self._gridMask):
            for colNumber, buttonText in enumerate(row):
                button = Button(buttonText)

                if not IsNumOrDot(buttonText) and not IsEmpty(buttonText):
                    button.setProperty("cssClass", "specialButton")
                    self._configSpecialButton(button)

                self.addWidget(button, rowNumber, colNumber)
                slot = self._makeSlot(
                    self._insertToDisplay,
                    buttonText,
                )
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button: Button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button: Button):
        text = button.text()

        if text == "C":
            self._connectButtonClicked(button, self._clear)

        if text in "+-/*^":
            self._connectButtonClicked(button, self._makeSlot(self._configLeftOp, text))
        if text == "=":
            self._connectButtonClicked(button, self._eq)

        if text == "◀":
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)

        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not IsValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._operator = None
        self.equation = self._equationInitialValue
        self.display.clear()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()
        self.display.clear()

        if text == "-" and len(displayText) == 0:
            self.display.insert(text)
            return

        if not IsValidNumber(displayText) and self._left is None:
            self._showError("Você não digitou nada.")
            return

        if self._left is None:
            self._left = convertToNumber(displayText)

        self._op = text
        self.equation = f"{self._left} {self._op} ??"

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not IsValidNumber(displayText):
            self._showError("Você não digitou o outro número da conta.")
            return

        self._right = convertToNumber(displayText)
        self.equation = f"{self._left} {self._op} {self._right}"
        result = "error"

        try:
            if "^" in self.equation and isinstance(self._left, float):  # type: ignore
                result = convertToNumber(math.pow(self._left, self._right))
            else:
                result = convertToNumber(eval(self.equation))

        except ZeroDivisionError:
            self._showError("Divisão por 0.")
        except OverflowError:
            self._showError("Essa conta não pode ser realizada.")

        self._left = result
        self.info.setText(f"{self.equation} = {result}")
        self.display.setText(str(result))

        if result == "error":
            self._left = None
            self._right = None
            self._operator = None
            self.display.clear()

    def _showError(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setWindowTitle("Error")
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.setStandardButtons(msgBox.StandardButton.Ok)
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        msgBox.setWindowTitle("Information")
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
