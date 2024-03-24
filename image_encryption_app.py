import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import os

class ImageEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Encryption and Decryption")
        
        # Styling
        self.master.config(bg="#f0f0f0")
        self.label_bg = "#f0f0f0"
        self.button_bg = "#008CBA"
        self.button_fg = "#ffffff"
        self.font = ("Helvetica", 12)
        
        # Image display area
        self.image_label = tk.Label(self.master, bg=self.label_bg)
        self.image_label.pack(pady=10)
        
        # Load Image button
        self.load_button = tk.Button(self.master, text="Load Image", command=self.load_image, bg=self.button_bg, fg=self.button_fg, font=self.font)
        self.load_button.pack(pady=5)
        
        # Encrypt Image button
        self.encrypt_button = tk.Button(self.master, text="Encrypt Image", command=self.encrypt_image, bg=self.button_bg, fg=self.button_fg, font=self.font)
        self.encrypt_button.pack(pady=5)
        
        # Decrypt Image button
        self.decrypt_button = tk.Button(self.master, text="Decrypt Image", command=self.decrypt_image_with_key, bg=self.button_bg, fg=self.button_fg, font=self.font)
        self.decrypt_button.pack(pady=5)
        
        # Load Encrypted Image button
        self.load_encrypted_button = tk.Button(self.master, text="Load Encrypted Image", command=self.load_encrypted_image_with_key, bg=self.button_bg, fg=self.button_fg, font=self.font)
        self.load_encrypted_button.pack(pady=5)
        
        # Encryption Algorithm dropdown menu
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("AES")
        self.algorithm_label = tk.Label(self.master, text="Encryption Algorithm", bg=self.label_bg, font=self.font)
        self.algorithm_label.pack()
        self.algorithm_option_menu = tk.OptionMenu(self.master, self.algorithm_var, "AES", "DES", "RSA")
        self.algorithm_option_menu.config(bg=self.button_bg, fg=self.button_fg, font=self.font)
        self.algorithm_option_menu.pack(pady=5)
        
        # Get the directory of the Python script
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        
        self.image_path = ""
        self.encrypted_image_path = ""
        self.decrypted_image_path = ""
        self.encryption_key_path = ""
        
    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
    
    def encrypt_image(self):
        if self.image_path:
            algorithm = self.algorithm_var.get()
            key = Fernet.generate_key()
            cipher = Fernet(key)
            with open(self.image_path, "rb") as f:
                data = f.read()
            encrypted_data = cipher.encrypt(data)
            # Save encrypted image and key
            self.encrypted_image_path = os.path.join(self.script_dir, "encrypted_image.encrypted")
            with open(self.encrypted_image_path, "wb") as f:
                f.write(encrypted_data)
            self.encryption_key_path = os.path.join(self.script_dir, "encryption_key.key")
            with open(self.encryption_key_path, "wb") as f:
                f.write(key)
            messagebox.showinfo("Encryption", "Image encrypted successfully!")
        else:
            messagebox.showerror("Error", "No image loaded!")
    
    def decrypt_image_with_key(self):
        key = simpledialog.askstring("Enter Key", "Enter the decryption key:")
        if key:
            self.decrypt_image(key)
    
    def decrypt_image(self, key):
        if self.encrypted_image_path:
            cipher = Fernet(key.encode())
            with open(self.encrypted_image_path, "rb") as f:
                encrypted_data = f.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            self.decrypted_image_path = os.path.join(self.script_dir, "decrypted_image.png")
            with open(self.decrypted_image_path, "wb") as f:
                f.write(decrypted_data)
            # Load and display decrypted image
            decrypted_image = Image.open(self.decrypted_image_path)
            decrypted_image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(decrypted_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            messagebox.showinfo("Decryption", "Image decrypted successfully!")
        else:
            messagebox.showerror("Error", "No encrypted image available!")
            
    def load_encrypted_image_with_key(self):
        self.encrypted_image_path = filedialog.askopenfilename(filetypes=[("Encrypted Image files", "*.encrypted")])
        if self.encrypted_image_path:
            messagebox.showinfo("Encrypted Image Loaded", "Encrypted image loaded successfully!")

def main():
    root = tk.Tk()
    app = ImageEncryptorDecryptor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
