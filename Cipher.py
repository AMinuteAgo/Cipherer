import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            unicode_offset = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - unicode_offset) % 26 + unicode_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_button_clicked():
    text = text_entry.get("1.0", "end-1c")
    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer")
        return
    encrypted_text = encrypt(text, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt_button_clicked():
    text = text_entry.get("1.0", "end-1c")
    try:
        shift = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer")
        return
    decrypted_text = decrypt(text, shift)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Cipher")

# Create input and output text widgets
text_label = tk.Label(root, text="Text:")
text_label.pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

key_label = tk.Label(root, text="Key:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_clicked)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_button_clicked)
decrypt_button.pack()

output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()