import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}|\;:',<.>/?`~"
pwd = ""


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        def generate_password():
            pwd = ""
            password_len = my_spin.value()
            for x in range(0,password_len):
                password_char = random.choice(chars)
                pwd = pwd + password_char
            my_pwd.setText(pwd)


        # Title
        self.setWindowTitle("Random Password Generator")

        # Layout
        self.setLayout(qtw.QVBoxLayout())

        # Label
        my_label = qtw.QLabel("Set the Password Length")
        # Set Font Size of the Label
        my_label.setFont(qtg.QFont('Courier New', 12))
        self.layout().addWidget(my_label)
        # Spin Box
        my_spin = qtw.QSpinBox(self, value=12, maximum=32, minimum=6, singleStep=12)
        self.layout().addWidget(my_spin)
        # Password Box Label
        pwd_label = qtw.QLabel("Your Secure Password")
        pwd_label.setFont(qtg.QFont('Courier New', 12))
        self.layout().addWidget(pwd_label)
        # Entry Box
        my_pwd = qtw.QLineEdit()
        my_pwd.setObjectName("Password")
        my_pwd.setText("Your Password Here")
        self.layout().addWidget(my_pwd)
        # Button
        my_button = qtw.QPushButton("Generate New Password", clicked=generate_password())
        self.layout().addWidget(my_button)


        self.show()

app = qtw.QApplication([])
mw = MainWindow()


app.exec_()