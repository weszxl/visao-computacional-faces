import cv2
import os

def face_capt(user):
    folder = f"data/{user}"
    os.makedirs(folder, exist_ok=True)
    capture = cv2.VideoCapture(0) # altere para 0 ou 1 
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    count = 0
    print("'Q' to end process.")
    
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        monochrome = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(monochrome, scaleFactor=1.2, minNeighbors=6)
        for (x, y, w, h) in faces:
            count += 1
            face = monochrome[y:y+h, x:x+w]
            file_path = os.path.join(folder, f"face_{count}.jpg")
            cv2.imwrite(file_path, face)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("capting_frames", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
            break
    capture.release()
    cv2.destroyAllWindows()
    print(f"ended. {count} frames. ")

p_name = input("Person name: ")
face_capt(p_name)





