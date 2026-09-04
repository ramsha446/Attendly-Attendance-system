import streamlit as st
import numpy as np

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashbaord
from src.components.footer import footer_dashboard
from PIL import Image
import time

from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embeddings
from src.database.db import get_all_students, create_student


def student_dashboard():
    student_data = st.session_state.student_data
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashbaord()
    with c2:
        st.markdown(
                f'<h3 style="color: black;">Welcome, {student_data["name"]}</h3>',
            unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()


    st.space()

    footer_dashboard()

def student_screen():

    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return
    
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

    show_registration = False
    photo_source = st.camera_input("position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome back! {student['name']}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header('Register new profile')
            new_name = st.text_input("Enter your name", placeholder="E.g. Ramsha Quareena")

            st.subheader('Optional: Voice Enrollment')
            st.info('Enroll your for voice only attendance')

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like Iam present, My name is Nazneen')
            except Exception as e:
                st.error('Audio data failed!')

            if st.button('Create account', type='primary'):
                if new_name:
                    with st.spinner('Creating your profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embeddings(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile created, Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Could'nt capture your facial features for registration")


                else:
                    st.warning('Please enter your name!')

    footer_dashboard()
