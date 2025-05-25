# QRCode-Scanner-Generator
A simple Python project to generate and scan QR codes using OpenCV and pyqrcode.
# QR Code Scanner & Generator

This Python project allows you to generate QR codes, scan QR codes from images, and scan them in real-time using a webcam.

📌 Features:

✅ QR Code Generator
- Generate QR codes from text, URL, or any string input
- Auto-save with short, unique filenames (`cat_142609.png`)
- Stores all QR codes in a dedicated folder (`generated_qrcodes/`)

✅ Image QR Scanner
- Scan all `.png` QR images from a folder
- Extract and print data for each code
- Handles invalid or unreadable images gracefully

 ✅ Webcam QR Scanner
- Real-time scanning using your webcam
- Each QR printed **only once**
- Optional sound on successful scan
- Draws bounding box + displays live decoded text

Requirements:

Install dependencies:

```bash
pip install -r requirements.txt
