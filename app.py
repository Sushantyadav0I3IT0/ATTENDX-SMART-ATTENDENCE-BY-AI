import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.Components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(
        page_title='ATTENDX - Making Attendance faster using AI',
        page_icon='http://localhost:8507/media/fe2b3917f15aafb5b7b5b50f2001d032.png',
    )

    # Initialize login state
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    # -----------------------------------------
    # 1. CHECK FOR CLASS JOIN LINK FIRST
    # -----------------------------------------
    join_code = st.query_params.get('join-code')

    if join_code:

        # If someone opens a class link,
        # force the application into student mode.
        if st.session_state.get('login_type') != 'student':
            st.session_state['login_type'] = 'student'
            st.rerun()

        # If student is already logged in,
        # open the enrollment dialog for this class.
        if (
            st.session_state.get('is_logged_in')
            and st.session_state.get('user_role') == 'student'
        ):
            auto_enroll_dialog(join_code)

            return

    # -----------------------------------------
    # 2. NORMAL APPLICATION ROUTING
    # -----------------------------------------
    match st.session_state['login_type']:

        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()


if __name__ == '__main__':
    main()