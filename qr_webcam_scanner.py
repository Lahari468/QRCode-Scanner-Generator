import cv2

def scan_qr_code_from_webcam():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    print("Press 'q' to quit.")
    last_data = ""       
    shown_data = set()   

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        
        if bbox is not None and data:

            for i in range(len(bbox[0])):
                pt1 = tuple(map(int, bbox[0][i]))
                pt2 = tuple(map(int, bbox[0][(i + 1) % len(bbox[0])]))
                cv2.line(frame, pt1, pt2, (255, 0, 0), 2)

            if data != last_data and data not in shown_data:
                print("QR Code data:", data)
                shown_data.add(data)
                last_data = data

            cv2.putText(frame, f"Data: {data}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)
        else:
            last_data = ""  

        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code_from_webcam()
