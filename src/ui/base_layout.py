import streamlit as st

def style_background_home():

    st.markdown("""
        <style>
                .stApp {
                    background-color: #EEF4F0 !important;
                }

                .stApp div[data-testid="stColumn"] {
                    background-color: #FFFFFF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }
        </style>

             """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
                .stApp {
                    background-color: #F5F6F8 !important;
                }
        </style>

             """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Valley+Sans:ital,wght@0,100..900;1,100..900&display=swap');

                /* Hide Top bar of streamlit */

                #MainMenu, header, footer {
                    visibility: hidden !important;
                }

                .block-container {
                   padding-top: 0.5rem !important;
                }

                h1 {
                    font-family: 'Climate Crisis', 'sans-serif' !important;
                    font-size: 3rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                }

                h2 {
                    font-family: 'Climate Crisis', 'sans-serif' !important;
                    font-size: 2rem !important;
                    line-height: 0.9 !important;
                    margin-bottom: 0rem !important;
                    color: black !important;
                }

                h3, h4, p {
                    font-family: 'Valley Sans', 'sans-serif' !important;
                }

                button {
                    border-radius: 1.5rem !important;
                    background-color: #5B5F97 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="secondary"] {
                    border-radius: 1.5rem !important;
                    background-color: #D98E73 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button[kind="tertiary"] {
                    border-radius: 1.5rem !important;
                    background-color: #343A40 !important;
                    color: white !important;
                    padding: 10px 20px !important;
                    border: none !important;
                    transition: transform 0.25s ease-in-out !important;
                }

                button:hover {
                transform: scale(1.05)
                }

             """, unsafe_allow_html=True)