import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import random
import json


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+[{]}|\;:',<.>/?`~"
pwd_list = {}
filename = "./temp/pwds.json"

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
            return pwd


        def save_password(self):
            pwd_cat = qtw.QInputDialog.getText(self, 'Save Password', 'Save Password As:')
            with open(filename) as pwds:
                pwd_list = json.load(pwds)
                pwd_list.append({"Category": pwd_cat, {"Password": pwd}})

        # Title
        self.setWindowTitle("Random Password Generator")

        # Layout
        self.setLayout(qtw.QVBoxLayout())

        # Password Length Spinbox Label
        my_label = qtw.QLabel("Set the Password Length")
        # Set Font Size of the Label
        my_label.setFont(qtg.QFont('Courier New', 12))
        self.layout().addWidget(my_label)
        # Password Length Spin Box
        my_spin = qtw.QSpinBox(self, value=12, maximum=32, minimum=6, singleStep=12)
        self.layout().addWidget(my_spin)
        # Generate Password Button
        my_button = qtw.QPushButton("Generate New Password")
        my_button.clicked.connect(generate_password)
        self.layout().addWidget(my_button)
        # Password Entry Box Label
        pwd_label = qtw.QLabel("Your Secure Password")
        pwd_label.setFont(qtg.QFont('Courier New', 12))
        self.layout().addWidget(pwd_label)
        # Password Entry Box
        my_pwd = qtw.QLineEdit()
        my_pwd.setObjectName("Password")
        my_pwd.setText("Your Password Here")
        self.layout().addWidget(my_pwd)
        # Save Password Button
        save_pwd_button = qtw.QPushButton("Save Password")
        save_pwd_button.clicked.connect(save_password)
        self.layout().addWidget(save_pwd_button)


        self.show()

app = qtw.QApplication([])
mw = MainWindow()


app.exec_()
