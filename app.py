import customtkinter as ctk


# Updated encryption and decryption logic
def rearrange(data):
    """Rearrange characters: reverse and split."""
    mid = len(data) // 2
    return data[mid:] + data[:mid]


def encrypt(plaintext, key):
    """Encrypt the plaintext with XOR and rearrangement."""
    encrypted_bytes = bytes([ord(c) ^ key for c in plaintext])
    encrypted_hex = encrypted_bytes.hex()
    rearranged = rearrange(encrypted_hex)
    return rearranged


def decrypt(ciphertext, key):
    """Decrypt the ciphertext with rearrangement and XOR."""
    rearranged_back = rearrange(ciphertext)  # Reverse rearrangement
    try:
        decrypted_bytes = bytes.fromhex(rearranged_back)
    except ValueError:
        return "Invalid ciphertext format."
    decrypted_chars = ''.join(chr(b ^ key) for b in decrypted_bytes)
    return decrypted_chars


# Enhanced GUI Implementation
class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure main window
        self.title("Custom Cryptography")
        self.geometry("600x500")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Title label
        self.title_label = ctk.CTkLabel(
            self,
            text="🔒 Custom Cryptography Tool",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

        # Input field for plaintext
        self.plaintext_label = ctk.CTkLabel(self, text="Input (Plaintext):", anchor="w")
        self.plaintext_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.plaintext_entry = ctk.CTkEntry(self, width=400)
        self.plaintext_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Input field for key
        self.key_label = ctk.CTkLabel(self, text="Key (Integer):", anchor="w")
        self.key_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        self.key_entry = ctk.CTkEntry(self, width=100)
        self.key_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # Output box for result
        self.result_label = ctk.CTkLabel(self, text="Result:", anchor="w")
        self.result_label.grid(row=3, column=0, padx=20, pady=10, sticky="e")

        self.result_box = ctk.CTkTextbox(self, height=100, width=400)
        self.result_box.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # Buttons for actions
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.encrypt_button = ctk.CTkButton(self.button_frame, text="Encrypt", command=self.encrypt_message)
        self.encrypt_button.grid(row=0, column=0, padx=10, pady=10)

        self.decrypt_button = ctk.CTkButton(self.button_frame, text="Decrypt", command=self.decrypt_message)
        self.decrypt_button.grid(row=0, column=1, padx=10, pady=10)

        # Footer
        self.footer_label = ctk.CTkLabel(
            self,
            text="Developed by 4LPH7 © 2025",
            font=ctk.CTkFont(size=12, slant="italic")
        )
        self.footer_label.grid(row=5, column=0, columnspan=2, pady=20)

    def encrypt_message(self):
        plaintext = self.plaintext_entry.get()
        key = self.key_entry.get()

        if not plaintext or not key.isdigit():
            self.result_box.delete("1.0", "end")
            self.result_box.insert("1.0", "Error: Please provide valid plaintext and key.")
            return

        key = int(key)
        encrypted = encrypt(plaintext, key)
        self.result_box.delete("1.0", "end")
        self.result_box.insert("1.0", encrypted)

    def decrypt_message(self):
        ciphertext = self.plaintext_entry.get()
        key = self.key_entry.get()

        if not ciphertext or not key.isdigit():
            self.result_box.delete("1.0", "end")
            self.result_box.insert("1.0", "Error: Please provide valid ciphertext and key.")
            return

        key = int(key)
        decrypted = decrypt(ciphertext, key)
        self.result_box.delete("1.0", "end")
        self.result_box.insert("1.0", decrypted)


# Run the enhanced app
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
    app = CryptoApp()
    app.mainloop()
