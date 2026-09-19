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

        /* ---------- MOBILE ---------- */

        @media (max-width: 768px) {

            .stApp div[data-testid="stColumn"] {
                padding: 1.2rem !important;
                border-radius: 2rem !important;
                margin-bottom: 1rem !important;
            }

            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }

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


        /* Hide Streamlit top bar */

        #MainMenu, header, footer {
            visibility: hidden !important;
        }


        /* Main container */

        .block-container {
            padding-top: 0.5rem !important;
        }


        /* Headings */

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3rem !important;
            line-height: 1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1 !important;
            margin-bottom: 0rem !important;
            color: black !important;
        }

        h3, h4, p {
            font-family: 'Valley Sans', sans-serif !important;
        }


        /* ---------- BUTTONS ---------- */

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
            transform: scale(1.03);
        }


        /* ---------- MOBILE RESPONSIVE ---------- */

        @media (max-width: 768px) {

            .block-container {
                padding-top: 0.5rem !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                padding-bottom: 1rem !important;
            }

            h1 {
                font-size: 2rem !important;
                line-height: 1.1 !important;
            }

            h2 {
                font-size: 1.5rem !important;
                line-height: 1.1 !important;
            }

            h3 {
                font-size: 1.2rem !important;
            }

            p {
                font-size: 0.95rem !important;
            }

            button {
                width: 100% !important;
                min-height: 45px !important;
                padding: 10px 14px !important;
                font-size: 0.95rem !important;
            }

            /* Reduce spacing on mobile */

            [data-testid="stHorizontalBlock"] {
                gap: 0.75rem !important;
            }

            /* Make images fit screen */

            img {
                max-width: 100% !important;
                height: auto !important;
            }

            h1 {
                font-size: 2rem !important;
            }

            [data-testid="stMarkdownContainer"] h1 {
                white-space: normal !important;
                text-align: center !important;
                word-break: normal !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>

            /* ================================
            MOBILE RESPONSIVE DESIGN
            Desktop design remains unchanged
            ================================ */

            @media (max-width: 768px) {

                /* ---------- MAIN PAGE ---------- */

                .block-container {
                    padding-top: 0.5rem !important;
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                    padding-bottom: 1rem !important;
                    max-width: 100% !important;
                }


                /* ---------- HEADINGS ---------- */

                h1 {
                    font-size: 2rem !important;
                    line-height: 1.1 !important;
                }

                h2 {
                    font-size: 1.5rem !important;
                    line-height: 1.2 !important;
                }

                h3 {
                    font-size: 1.2rem !important;
                    line-height: 1.2 !important;
                }

                h4 {
                    font-size: 1.05rem !important;
                }

                p {
                    font-size: 0.95rem !important;
                }


                /* ---------- STREAMLIT COLUMNS ---------- */

                /*
                On mobile, columns become full-width.
                So 2-column / 3-column / 4-column layouts
                don't get squeezed.
                */

                [data-testid="stHorizontalBlock"] {
                    flex-wrap: wrap !important;
                    gap: 0.8rem !important;
                }

                [data-testid="stHorizontalBlock"] > [data-testid="column"] {
                    width: 100% !important;
                    min-width: 100% !important;
                    flex: 1 1 100% !important;
                }


                /* ---------- BUTTONS ---------- */

                [data-testid="stButton"] {
                    width: 100% !important;
                }

                [data-testid="stButton"] > button {
                    width: 100% !important;
                    min-height: 46px !important;
                    padding: 10px 14px !important;
                    font-size: 0.95rem !important;
                    white-space: normal !important;
                    line-height: 1.2 !important;
                }


                /* ---------- INPUT BOXES ---------- */

                [data-testid="stTextInput"],
                [data-testid="stNumberInput"],
                [data-testid="stSelectbox"],
                [data-testid="stMultiSelect"],
                [data-testid="stDateInput"],
                [data-testid="stFileUploader"] {
                    width: 100% !important;
                }


                /* ---------- TEXT INPUT ---------- */

                [data-testid="stTextInput"] input {
                    width: 100% !important;
                    font-size: 16px !important;
                    min-height: 42px !important;
                    box-sizing: border-box !important;
                }


                /* ---------- SELECT BOX ---------- */

                [data-testid="stSelectbox"] > div {
                    width: 100% !important;
                }


                /* ---------- FILE UPLOADER ---------- */

                [data-testid="stFileUploader"] {
                    width: 100% !important;
                }


                /* ---------- IMAGES ---------- */

                img {
                    max-width: 100% !important;
                    height: auto !important;
                }


                /* ---------- DATAFRAMES / TABLES ---------- */

                [data-testid="stDataFrame"] {
                    width: 100% !important;
                    overflow-x: auto !important;
                }


                /* ---------- ALERTS / INFO / SUCCESS / ERROR ---------- */

                [data-testid="stAlert"] {
                    width: 100% !important;
                    box-sizing: border-box !important;
                }


                /* ---------- EXPANDERS ---------- */

                [data-testid="stExpander"] {
                    width: 100% !important;
                }


                /* ---------- MARKDOWN CONTENT ---------- */

                [data-testid="stMarkdownContainer"] {
                    max-width: 100% !important;
                    overflow-wrap: break-word !important;
                }


                /* ---------- HOME PAGE CARDS ---------- */

                .stApp div[data-testid="stColumn"] {
                    padding: 1.2rem !important;
                    border-radius: 2rem !important;
                    box-sizing: border-box !important;
                }


                /* ---------- HEADER TITLE ---------- */

                .attendly-home-title {
                    white-space: normal !important;
                    text-align: center !important;
                    font-size: 2rem !important;
                    line-height: 1.05 !important;
                    word-break: normal !important;
                    overflow-wrap: normal !important;
                }


                /* Dashboard/header title should NOT break
                into ATT / END / LY */

                .attendly-dashboard-title {
                    white-space: nowrap !important;
                    font-size: 2rem !important;
                    line-height: 1 !important;
                    flex-shrink: 0 !important;
                }


                /* ---------- FOOTER ---------- */

                footer {
                    width: 100% !important;
                    text-align: center !important;
                }


                /* ---------- REMOVE HORIZONTAL OVERFLOW ---------- */

                html,
                body,
                .stApp {
                    max-width: 100% !important;
                    overflow-x: hidden !important;
                }

            }

        </style>
            """, unsafe_allow_html=True)