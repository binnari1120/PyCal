import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt

class Main (QWidget):
    def __init__(self):
        super().__init__()

        self.lEdit_display = QLineEdit(self)
        self.lEdit_display.setReadOnly(True)

        self.action_is_clicked = False
        self.arithmetic_operator = ""

        self.input_value = 0
        self.temporal_value = 0
        self.output_value = 0

        self.initUI()
        self.initSlot()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("PyCalculator")

        layout = QGridLayout(self)
        layout.setSpacing(10)

        layout.addWidget(self.lEdit_display, 0, 0, 1, 5)

        btn_texts = [
            "C", "+/-", "%", "/",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", "", ".", "="
        ]
        btn_positions = []
        for i in range(1, 6):
            for j in range(0, 4):
                btn_positions.append((i,j))
        # positions = [ (i, j) for i in range(5) for j in range(4) ]

        self.btns = []
        for btn_positions, btn_text in zip(btn_positions, btn_texts):
            if btn_text == "":
                continue
            btn = QPushButton(btn_text, self)
            layout.addWidget(btn, *btn_positions)
            self.btns.append(btn)

        self.show()


    def initSlot(self):
        for i in range(len(self.btns)):
            self.btns[i].clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        sender = self.sender()
        if sender.text() == "C":
            self.action_is_clicked = False
            self.arithmetic_operator = ""
            self.input_value = 0
            self.temporal_value = 0
        elif sender.text() in ["+", "-", "x", "/"]:
            self.action_is_clicked = True
            self.arithmetic_operator = sender.text()
            self.temporal_value = self.output_value + self.input_value
            print("Temporal value: ", self.temporal_value)
        elif sender.text() == "=":
            if self.arithmetic_operator == "+":
                self.output_value = self.temporal_value + self.input_value
            elif self.arithmetic_operator == "-":
                self.output_value = self.temporal_value - self.input_value
            elif self.arithmetic_operator == "x":
                self.output_value = self.temporal_value * self.input_value
            elif self.arithmetic_operator == "/":
                self.output_value = self.temporal_value / self.input_value

            self.lEdit_display.setText(str(self.output_value))
            print("Output value: ", self.output_value)

            self.action_is_clicked = False
            self.arithmetic_operator = ""
            self.input_value = 0
            self.temporal_value = 0
        else:
            if self.action_is_clicked == True:
                self.action_is_clicked = False
                self.lEdit_display.setText(sender.text())
                self.input_value = int(self.lEdit_display.text())
                print("Input value: ", self.input_value)
            else:
                self.lEdit_display.setText(self.lEdit_display.text()+sender.text())
                self.input_value = int(self.lEdit_display.text())
                print("Input value: ", self.input_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    app.exec_()
    sys.exit()
