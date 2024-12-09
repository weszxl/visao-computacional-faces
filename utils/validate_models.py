import pickle

file = "models/recognition_model.pkl"

try:
    with open(file, "rb") as f:
        data = pickle.load(f)
    print("file ok")
    print("data:", data)
except EOFError:
    print("error file is empty/corrupt.")
except Exception as e:
    print(f"unknow error: {e}")


