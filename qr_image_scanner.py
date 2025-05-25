import cv2
import os

QR_FOLDER = "generated_qrcodes"  
SHOW_IMAGE = False      

def scan_qr_code_from_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Could not load: {image_path}")
        return

    if SHOW_IMAGE:
        cv2.imshow("QR Code", img)
        cv2.waitKey(500)  
        cv2.destroyAllWindows()

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print(f"✅ {os.path.basename(image_path)} → {data}")
    else:
        print(f"⚠️ No QR code in {os.path.basename(image_path)}")

def scan_all_qr_codes(folder):
    if not os.path.exists(folder):
        print(f"❌ Folder '{folder}' does not exist.")
        return

    png_files = [f for f in os.listdir(folder) if f.endswith(".png")]
    if not png_files:
        print("⚠️ No PNG files found in the folder.")
        return

    for file in png_files:
        scan_qr_code_from_image(os.path.join(folder, file))

if __name__ == "__main__":
    scan_all_qr_codes(QR_FOLDER)
