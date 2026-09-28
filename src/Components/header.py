import streamlit as st
from pathlib import Path


def header_home():

    logo_path = Path(__file__).resolve().parent / "logo" / "logo.png"
    st.markdown(
        """
        <style>
            .st-key-attendx-brand {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
                margin: 0 auto 1rem;
            }

            .st-key-attendx-brand div[data-testid="stImage"] {
                display: flex;
                justify-content: center;
                width: 100%;
                margin: 0;
            }

            .st-key-attendx-brand div[data-testid="stImage"] img {
                width: 110px !important;
                height: 110px !important;
                object-fit: contain;
            }

            .attendx-title {
                color: #E0E3FF;
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2.75rem !important;
                line-height: 1;
                text-align: center;
                margin: 0.35rem 0 1.5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container(key="attendx-brand"):
        st.image(str(logo_path), width=100)
        st.markdown("<h1 class='attendx-title'>ATTENDX</h1>", unsafe_allow_html=True)


def header_dashboard():

    logo_path = Path(__file__).resolve().parent / "logo" / "logo.png"

    st.markdown(
        """
        <style>
            .st-key-dashboard-brand {
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
            }

            .st-key-dashboard-brand div[data-testid="stImage"] {
                display: flex;
                justify-content: center;
                width: 100%;
            }

            .st-key-dashboard-brand h2 {
                color: #5865F2 !important;
                margin: 0;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container(key="dashboard-brand"):
        st.image(str(logo_path), width=85)
        st.markdown("<h2>AttendX</h2>", unsafe_allow_html=True)