import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st

from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:
        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        encodings.append(np.array(face_descriptor))

    return encodings


@st.cache_resource
def get_trained_model():
    X = []
    y = []

    # Get students from Supabase
    student_db = get_all_students()

    print("Students from DB:", len(student_db))

    if not student_db:
        return None

    # Load face embeddings
    for student in student_db:
        embedding = student.get("face_embedding")

        if embedding:
            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    print("Embeddings loaded:", len(X))
    print("Student IDs:", y)

    if len(X) == 0:
        return None

    # Train SVC
    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    try:
        clf.fit(X, y)
    except ValueError as e:
        print("SVC training error:", e)
        return None

    return {
        "clf": clf,
        "X": X,
        "y": y
    }


def train_classifier():
    st.cache_resource.clear()

    model_data = get_trained_model()

    return bool(model_data)


def predict_attendance(class_image_np):

    # Detect faces and generate embeddings
    encodings = get_face_embeddings(class_image_np)

    print("Faces detected:", len(encodings))

    detected_student = {}

    if not encodings:
        return detected_student, [], 0

    # Load trained model
    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    clf = model_data["clf"]

    X_train = np.asarray(
        model_data["X"],
        dtype=float
    )

    y_train = model_data["y"]

    all_students = sorted(
        set(int(student_id) for student_id in y_train)
    )

    # Compare every detected face
    # against every registered face embedding
    for encoding in encodings:

        encoding = np.asarray(
            encoding,
            dtype=float
        )

        if X_train.size == 0:
            continue

        distances = np.linalg.norm(
            X_train - encoding,
            axis=1
        )

        # Closest registered face
        best_index = int(
            np.argmin(distances)
        )

        predicted_id = int(
            y_train[best_index]
        )

        best_match_score = float(
            distances[best_index]
        )

        resemblance_threshold = 0.50

        print(
            f"Predicted ID: {predicted_id}, "
            f"Face distance: {best_match_score:.4f}, "
            f"Threshold: {resemblance_threshold}"
        )

        # Accept only if similarity is good enough
        if best_match_score <= resemblance_threshold:
            detected_student[predicted_id] = True

        else:
            print(
                f"Unknown face. "
                f"Best distance: {best_match_score:.4f}"
            )

    return (
        detected_student,
        all_students,
        len(encodings)
    )
