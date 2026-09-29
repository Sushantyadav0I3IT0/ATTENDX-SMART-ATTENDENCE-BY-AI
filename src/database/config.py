import os

import streamlit as st
from supabase import Client, create_client


def _get_secret(key: str) -> str:
    value = st.secrets.get(key, os.getenv(key)) if hasattr(st, "secrets") else os.getenv(key)
    if not value:
        raise RuntimeError(
            f"Missing required secret '{key}'. "
            "Set it in .streamlit/secrets.toml locally or in Streamlit Cloud secrets."
        )
    return value


supabase: Client = create_client(
    _get_secret("SUPABASE_URL"),
    _get_secret("SUPABASE_KEY"),
)