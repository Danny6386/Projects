from PyQt5 import QtWidgets, QtGui, QtCore
import sys

# Functions for encryption and decryption
def vigenere(message, key, direction):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`-=~_+[]{};:,.<>/? '"
    final_message = ''

    for char in message.lower():
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset * direction) % len(alphabet)
        final_message += alphabet[new_index]

    return final_message

def decrypt(message, key):
    return vigenere(message, key, -1)

def encrypt(message, key):
    return vigenere(message, key, 1)

# Main GUI Application
class EncryptionApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Encrypter and Decrypter")
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")

        # Main layout
        layout = QtWidgets.QVBoxLayout()
        
        # Title Label
        self.title_label = QtWidgets.QLabel("Advanced Encrypter and Decrypter")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #00ffcc;")

        # Dropdown for encryption or decryption
        self.mode_label = QtWidgets.QLabel("Choose Mode:")
        self.mode_combo = QtWidgets.QComboBox()
        self.mode_combo.addItems(["Encrypt", "Decrypt"])
        self.mode_combo.setStyleSheet("background-color: #444444; color: #ffffff; border: 1px solid #00ffcc; padding: 5px;")

        # Input fields for text and key
        self.text_label = QtWidgets.QLabel("Enter Message:")
        self.text_input = QtWidgets.QTextEdit()
        self.text_input.setStyleSheet("background-color: #444444; color: #ffffff; border: 1px solid #00ffcc; padding: 5px;")
        
        self.key_label = QtWidgets.QLabel("Enter Key:")
        self.key_input = QtWidgets.QLineEdit()
        self.key_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key_input.setStyleSheet("background-color: #444444; color: #ffffff; border: 1px solid #00ffcc; padding: 5px;")

        # Output field
        self.result_label = QtWidgets.QLabel("Result:")
        self.result_output = QtWidgets.QTextEdit()
        self.result_output.setReadOnly(True)
        self.result_output.setStyleSheet("background-color: #444444; color: #00ffcc; border: 1px solid #00ffcc; padding: 5px;")
        
        # Action buttons with rounded corners
        self.run_button = QtWidgets.QPushButton("Run")
        self.run_button.clicked.connect(self.run_operation)
        self.run_button.setStyleSheet("""
            QPushButton {
                background-color: #00ffcc;
                color: #2e2e2e;
                padding: 10px;
                font-weight: bold;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #00ccaa;
            }
        """)

        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #333333;
                color: #00ffcc;
                padding: 10px;
                font-weight: bold;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #444444;
            }
        """)

        # Quit button with rounded corners
        self.quit_button = QtWidgets.QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d;
                color: #ffffff;
                padding: 10px;
                font-weight: bold;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #cc3b3b;
            }
        """)

        # Add widgets to layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.text_label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.key_label)
        layout.addWidget(self.key_input)
        layout.addWidget(self.run_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

    def run_operation(self):
        # Get values from input fields
        mode = self.mode_combo.currentText()
        text = self.text_input.toPlainText()
        key = self.key_input.text()

        # Check if inputs are valid
        if not text or not key:
            self.result_output.setText("Please enter both a message and a key.")
            return

        # Perform encryption or decryption
        if mode == "Encrypt":
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        # Display result
        self.result_output.setText(result)

    def clear_fields(self):
        # Clear all input and output fields
        self.text_input.clear()
        self.key_input.clear()
        self.result_output.clear()

# Run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())
