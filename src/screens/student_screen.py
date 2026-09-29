import time

import numpy as np
import streamlit as st
from PIL import Image

from src.Ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
)

from src.Components.header import header_dashboard
from src.Components.footer import footer_dashboard
from src.Components.dialog_enroll import enroll_dialog
from src.Components.subject_card import subject_card

from src.pipelines.face_pipeline import (
    predict_attendance,
    get_face_embeddings,
    train_classifier,
)

from src.pipelines.voice_pipeline import get_voice_embedding

from src.database.db import (
    get_all_students,
    create_student,
    get_student_subjects,
    get_student_attendance,
    unenroll_student_to_subject,
)


# ============================================================
# STUDENT DASHBOARD
# ============================================================

def student_dashboard():

    student_data = st.session_state.student_data
    student_id = student_data["student_id"]

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:
        st.subheader(
            f"Welcome, {student_data['name']}"
        )

        if st.button(
            "Logout",
            type="secondary",
            key="student_logout_btn",
            shortcut="control+backspace",
        ):
            st.session_state["is_logged_in"] = False

            if "student_data" in st.session_state:
                del st.session_state["student_data"]

            st.rerun()

    st.space()

    # --------------------------------------------------------
    # Subjects Header
    # --------------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:
        st.header("Your Enrolled Subjects")

    with c2:
        if st.button(
            "Enroll in Subject",
            type="primary",
            width="stretch",
            key="enroll_subject_btn",
        ):
            enroll_dialog()

    st.divider()

    # --------------------------------------------------------
    # Load subjects and attendance
    # --------------------------------------------------------

    with st.spinner("Loading your enrolled subjects.."):

        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    # --------------------------------------------------------
    # Calculate attendance statistics
    # --------------------------------------------------------

    stats_map = {}

    for log in logs:

        sid = log["subject_id"]
        class_timestamp = log.get("timestamp")

        if sid not in stats_map:
            stats_map[sid] = {
                "classes": set(),
                "attended_classes": set(),
            }

        if class_timestamp:
            stats_map[sid]["classes"].add(class_timestamp)

            if log.get("is_present"):
                stats_map[sid]["attended_classes"].add(class_timestamp)

    # --------------------------------------------------------
    # Subject cards
    # --------------------------------------------------------

    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):

        sub = sub_node["subjects"]

        subject_id = sub["subject_id"]

        stats = stats_map.get(
            subject_id,
            {
                "classes": set(),
                "attended_classes": set(),
            },
        )

        # ----------------------------------------------------
        # Unenroll callback
        # ----------------------------------------------------

        def unenroll_button(
            current_subject_id=subject_id,
            current_subject_name=sub["name"],
            card_index=i,
        ):

            if st.button(
                "Unenroll from this course",
                type="tertiary",
                width="stretch",
                key=f"unenroll_{student_id}_{current_subject_id}_{card_index}",
                icon=":material/delete_forever:",
            ):

                unenroll_student_to_subject(
                    student_id,
                    current_subject_id,
                )

                st.toast(
                    f"Unenrolled from {current_subject_name} successfully!"
                )

                st.rerun()

        # ----------------------------------------------------
        # Render subject card
        # ----------------------------------------------------

        with cols[i % 2]:

            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],
                stats=[
                    (
                        "✅",
                        "Classes attended",
                        f"{len(stats['attended_classes'])} / {len(stats['classes'])}",
                    ),
                ],
                footer_callback=unenroll_button,
            )

    footer_dashboard()


# ============================================================
# STUDENT SCREEN
# ============================================================

def student_screen():

    style_background_dashboard()
    style_base_layout()

    # --------------------------------------------------------
    # Already logged-in student
    # --------------------------------------------------------

    if "student_data" in st.session_state:

        student_dashboard()

        return

    # --------------------------------------------------------
    # Login Header
    # --------------------------------------------------------

    c1, c2 = st.columns(
        2,
        vertical_alignment="center",
        gap="xxlarge",
    )

    with c1:
        header_dashboard()

    with c2:

        if st.button(
            "Go back to Home",
            type="secondary",
            key="student_home_btn",
            shortcut="control+backspace",
        ):

            st.session_state["login_type"] = None

            st.rerun()

    # --------------------------------------------------------
    # Face Login
    # --------------------------------------------------------

    st.header(
        "Login using FaceID",
        text_alignment="center",
    )

    st.space()
    st.space()

    show_registration = False

    photo_source = st.camera_input(
        "Position your face in the center"
    )

    # --------------------------------------------------------
    # Face Recognition
    # --------------------------------------------------------

    if photo_source:

        img = np.array(
            Image.open(photo_source)
        )

        with st.spinner("AI is scanning.."):

            detected, all_ids, num_faces = predict_attendance(
                img
            )

        # No face detected
        if num_faces == 0:

            st.warning(
                "Face not found!"
            )

        # Known face detected
        elif detected:

            if len(detected) > 1:

                st.info(
                    f"Detected {len(detected)} known faces "
                    "in this photo. Please use a single-person "
                    "photo for login."
                )

            else:

                student_id = list(
                    detected.keys()
                )[0]

                all_students = get_all_students()

                student = next(
                    (
                        s
                        for s in all_students
                        if s["student_id"] == student_id
                    ),
                    None,
                )

                if student:

                    st.session_state["is_logged_in"] = True
                    st.session_state["user_role"] = "student"
                    st.session_state["student_data"] = student

                    st.toast(
                        f"Welcome Back {student['name']}"
                    )

                    time.sleep(1)

                    st.rerun()

        # Unknown face
        else:

            st.info(
                "Face not recognized! "
                "You might be a new student!"
            )

            show_registration = True

    # --------------------------------------------------------
    # New Student Registration
    # --------------------------------------------------------

    if show_registration:

        with st.container(border=True):

            st.header(
                "Register new Profile"
            )

            new_name = st.text_input(
                "Enter your name",
                placeholder="E.g. Hamza Rizvi",
                key="new_student_name",
            )

            st.subheader(
                "Optional : Voice Enrollment"
            )

            st.info(
                "Enroll your voice for voice-only attendance"
            )

            audio_data = None

            try:

                audio_data = st.audio_input(
                    "Record a short phrase like "
                    "'I am present' or "
                    "'My name is Akash'.",
                    key="voice_registration",
                )

            except Exception:

                st.error(
                    "Audio Data failed!"
                )

            # ------------------------------------------------
            # Create Account
            # ------------------------------------------------

            if st.button(
                "Create Account",
                type="primary",
                key="create_student_account_btn",
            ):

                if new_name:

                    with st.spinner(
                        "Creating profile.."
                    ):

                        # Get face embedding
                        img = np.array(
                            Image.open(photo_source)
                        )

                        encodings = get_face_embeddings(
                            img
                        )

                        if encodings:

                            face_emb = encodings[
                                0
                            ].tolist()

                            # --------------------------------
                            # Voice embedding
                            # --------------------------------

                            voice_emb = None

                            if audio_data:

                                voice_emb = get_voice_embedding(
                                    audio_data.read()
                                )

                            # --------------------------------
                            # Save student
                            # --------------------------------

                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb,
                                voice_embedding=voice_emb,
                            )

                            if response_data:

                                # Clear/retrain face model
                                train_classifier()

                                st.session_state[
                                    "is_logged_in"
                                ] = True

                                st.session_state[
                                    "user_role"
                                ] = "student"

                                st.session_state[
                                    "student_data"
                                ] = response_data[0]

                                st.toast(
                                    f"Profile Created! "
                                    f"Hi {new_name}!"
                                )

                                time.sleep(1)

                                st.rerun()

                        else:

                            st.error(
                                "Couldn't capture your "
                                "facial features for registration"
                            )

                else:

                    st.warning(
                        "Please enter your name!"
                    )

    footer_dashboard()