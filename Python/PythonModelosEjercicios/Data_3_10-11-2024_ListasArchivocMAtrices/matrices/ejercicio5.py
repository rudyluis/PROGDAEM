import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Suma de Dos Números")
        self.setGeometry(300, 300, 300, 200)

        self.label_num1 = QLabel("Número 1:", self)
        self.label_num1.move(50, 30)

        self.textbox_num1 = QLineEdit(self)
        self.textbox_num1.move(150, 30)

        self.label_num2 = QLabel("Número 2:", self)
        self.label_num2.move(50, 70)

        self.textbox_num2 = QLineEdit(self)
        self.textbox_num2.move(150, 70)

        self.label_result = QLabel("Resultado:", self)
        self.label_result.move(50, 110)

        self.button_sum = QPushButton("Sumar", self)
        self.button_sum.move(150, 130)
        self.button_sum.clicked.connect(self.sumar_numeros)
        
        self.combo_paises = QComboBox(self)
        self.combo_paises.addItem("Argentina")
        self.combo_paises.addItem("Brasil")
        self.combo_paises.addItem("Chile")
        self.combo_paises.move(150, 150)

        layout = QVBoxLayout()
        layout.addWidget(self.label_num1)
        layout.addWidget(self.textbox_num1)
        layout.addWidget(self.label_num2)
        layout.addWidget(self.textbox_num2)
        layout.addWidget(self.label_result)
        layout.addWidget(self.button_sum)
        layout.addWidget(self.combo_paises)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def sumar_numeros(self):
        num1 = float(self.textbox_num1.text())
        num2 = float(self.textbox_num2.text())
        resultado = num1 + num2
        self.label_result.setText("Resultado: " + str(resultado))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
