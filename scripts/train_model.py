import face_recognition
import os
import pickle

def training_capture(data_dir="data/"):
    know_face = []
    know_name = []
    for names in os.listdir(data_dir):
        user_folder = os.path.join(data_dir, names)
        if not os.path.isdir(user_folder):
            continue
        for file in os.listdir(user_folder):
            image_path = os.path.join(user_folder, file)
            image = face_recognition.load_image_file(image_path)
            try:
                encodings = face_recognition.face_encodings(image)[0]
                know_face.append(encodings)
                know_name.append(names)
            except IndexError:
                print(f"unrecognized face({image_path})...")
    with open("models/recognition_model.pkl", "wb") as training_file:
        training_data = {"names": know_name, "encodings": know_face}
        pickle.dump(training_data, training_file)
    print("end training process")

training_capture()

