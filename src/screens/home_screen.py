import streamlit as st
from pathlib import Path
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout
from src.components.footer import footer_home


def home_screen():

    header_home()

    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        student_image = Path(__file__).resolve().parents[2] / "student.png"
        st.image(str(student_image), width=200)
        if st.button('Student portal', type="primary", icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        teacher_image = Path(__file__).resolve().parents[2] / "teacher.png"
        st.image(str(teacher_image), width=200)
        if st.button('Teacher portal', type="primary", icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()
        

            