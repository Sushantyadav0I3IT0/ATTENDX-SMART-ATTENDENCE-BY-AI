import streamlit as st

from src.database.db import delete_subject


@st.dialog("Delete subject")
def delete_subject_dialog(subject_id, subject_name, subject_code, teacher_id):
    st.warning(
        f"Delete {subject_name} ({subject_code})? This permanently removes "
        "its enrollments and attendance history. This cannot be undone."
    )

    cancel_column, delete_column = st.columns(2)

    with cancel_column:
        if st.button("Cancel", key=f"cancel_delete_subject_{subject_id}", width="stretch"):
            st.rerun()

    with delete_column:
        if st.button(
            "Delete subject",
            key=f"confirm_delete_subject_{subject_id}",
            type="primary",
            width="stretch",
            icon=":material/delete_forever:",
        ):
            try:
                delete_subject(subject_id, teacher_id)
                if st.session_state.get("attendance_subject_filter") == subject_id:
                    st.session_state["attendance_subject_filter"] = None
                st.toast(f"{subject_name} was deleted.")
                st.rerun()
            except Exception as error:
                st.error(f"Could not delete subject: {error}")