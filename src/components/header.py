import streamlit as st
import base64
from pathlib import Path

def header_home():

    logo_path = Path(__file__).resolve().parents[2] / "logo.png"

    with open(logo_path, "rb") as f:
        logo_url = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"

    st.markdown(f"""
        <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 1px; margin-top: 20px;'>
            <img src='{logo_url}' style= 'height: 100px'; />
            <h1 style='text-align: center; color: #3046A5; white-space: nowrap;'>Welcome to, ATTENDLY</h1>
        </div>

                    """, unsafe_allow_html=True)


def header_dashbaord():

    logo_path = Path(__file__).resolve().parents[2] / "logo.png"
    
    with open(logo_path, "rb") as f:
        logo_url = f"data:image/png;base64,{base64.b64encode(f.read()).decode()}"

    st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: center; gap: 10px;'>
            <img src='{logo_url}' style= 'height: 85px'; />
            <h1 style='text-align: left; color: #3046A5; white-space: nowrap;'>ATTENDLY</h1>
        </div>

                    """, unsafe_allow_html=True)