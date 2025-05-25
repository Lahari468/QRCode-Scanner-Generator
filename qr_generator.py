import pyqrcode
import time
import os

def sanitize_filename(data):
    
    return "".join(c if c.isalnum() else "_" for c in data[:8])

def generate_qr(data, folder="generated_qrcodes"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    
    timestamp = time.strftime("%H%M%S")
    filename = f"{sanitize_filename(data)}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    qr = pyqrcode.create(data)
    qr.png(filepath, scale=6)
    print(f"QR code saved as {filepath}")

if __name__ == "__main__":
    data = input("Enter text or URL to encode in QR code: ")
    generate_qr(data)
