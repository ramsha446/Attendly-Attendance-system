import streamlit as st
import numpy as np

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashbaord
from src.components.footer import footer_dashboard
from PIL import Image

def student_screen():

    style_background_dashboard()
    style_base_layout()


    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashbaord()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()
                    

    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()
    st.markdown("""
                <style>
                    [data-testid="stCameraInput"] label,
                    [data-testid="stCameraInput"] label p {
                        color: black !important;
                    }
                </style>
                    """, unsafe_allow_html=True)
    photo_source = st.camera_input("position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning'):
            detected, all_ids, num_faces = predict_attendance(img)

    footer_dashboard()
