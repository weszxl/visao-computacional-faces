import cv2
import face_recognition
import pickle
import numpy as np

def identify_face():
    with open("models/recognition_model.pkl", "rb") as training_file:
        training_data = pickle.load(training_file)
    know_names = training_data["names"]
    know_enconding = np.array(training_data["encodings"])
    if len(know_enconding) == 0:
        raise ValueError("no encoding found")
    capture_video = cv2.VideoCapture(0) # altere para 0 ou 1 
    if not capture_video.isOpened():
        raise Exception("webcam has a problem")
    print("inicializing... 'Q' to break process")

    try:
        while True:
            ret, frame = capture_video.read()
            if not ret:
                print("unable frame")
                break
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            localize_frame_face = face_recognition.face_locations(rgb_frame)
            encodings = []
            for face_location in localize_frame_face:
                encoding = face_recognition.face_encodings(rgb_frame, [face_location])
                if encoding:
                    encodings.append(encoding[0])
            for (top, right, bottom, left), encoding in zip(localize_frame_face, encodings):
                matches = face_recognition.compare_faces(know_enconding, encoding)
                name = "Unknow"
                if True in matches:
                    match_index = matches.index(True)
                    name = know_names[match_index]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            cv2.imshow("recognized frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        capture_video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    identify_face()
