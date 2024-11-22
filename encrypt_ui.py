import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to perform Vigenere cipher encryption and decryption
def vigenere(message, key, direction):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`-=~_+[]{};:,.<>/?' "
    final_message = ''

    for char in message.lower():
        key_char = key[key_index % len(key)]
        key_index += 1

        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset * direction) % len(alphabet)
        final_message += alphabet[new_index]

    return final_message

# Encrypt and decrypt functions using Vigenere
def encrypt(message, key):
    return vigenere(message, key, 1)

def decrypt(message, key):
    return vigenere(message, key, -1)

# GUI class to create the interface
class EncryptDecryptGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Encrypter and Decrypter - Dark Mode")
        self.root.geometry("550x300")
        self.root.resizable(False, False)

        # Configure style for ttk widgets for dark mode
        style = ttk.Style()
        style.theme_use("clam")
        
        # Dark mode colors
        dark_bg = "#2E2E2E"
        dark_fg = "#D1D1D1"
        accent_color = "#4CAF50"

        # Set background color
        self.root.configure(bg=dark_bg)
        
        style.configure("TLabel", background=dark_bg, foreground=dark_fg, font=("Arial", 12))
        style.configure("TEntry", background=dark_bg, foreground=dark_fg, font=("Arial", 11), fieldbackground=dark_bg)
        style.configure("TText", background=dark_bg, foreground=dark_fg, font=("Arial", 11))
        style.configure("TButton", background=accent_color, foreground=dark_fg, font=("Arial", 11), padding=5)
        style.map("TButton", background=[("active", accent_color)])

        # Main frame
        main_frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input label and entry for message text
        ttk.Label(main_frame, text="Enter your message:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.message_entry = ttk.Entry(main_frame, width=50, foreground=dark_fg)
        self.message_entry.grid(row=0, column=1, padx=5, pady=5)

        # Input label and entry for key
        ttk.Label(main_frame, text="Enter your secret key:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.key_entry = ttk.Entry(main_frame, width=50, foreground=dark_fg)
        self.key_entry.grid(row=1, column=1, padx=5, pady=5)

        # Output label and text field for results
        ttk.Label(main_frame, text="Output:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.output_text = tk.Text(main_frame, height=5, width=50, wrap='word', font=("Arial", 11), bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
        self.output_text.grid(row=2, column=1, padx=5, pady=5)

        # Button frame
        button_frame = ttk.Frame(main_frame, padding="10 0 0 0", style="TFrame")
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # Encrypt button
        encrypt_button = ttk.Button(button_frame, text="Encrypt", command=self.encrypt_message, width=15)
        encrypt_button.grid(row=0, column=0, padx=5, pady=5)

        # Decrypt button
        decrypt_button = ttk.Button(button_frame, text="Decrypt", command=self.decrypt_message, width=15)
        decrypt_button.grid(row=0, column=1, padx=5, pady=5)

        # Quit button
        quit_button = ttk.Button(button_frame, text="Quit", command=root.quit, width=15)
        quit_button.grid(row=0, column=2, padx=5, pady=5)

    # Function to encrypt the message
    def encrypt_message(self):
        message = self.message_entry.get()
        key = self.key_entry.get()
        if not key or not message:
            messagebox.showerror("Input Error", "Both message and key are required.")
            return
        encrypted_text = encrypt(message, key)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, encrypted_text)

    # Function to decrypt the message
    def decrypt_message(self):
        message = self.message_entry.get()
        key = self.key_entry.get()
        if not key or not message:
            messagebox.showerror("Input Error", "Both message and key are required.")
            return
        decrypted_text = decrypt(message, key)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, decrypted_text)

# Initialize the GUI application
root = tk.Tk()
app = EncryptDecryptGUI(root)
root.mainloop()
