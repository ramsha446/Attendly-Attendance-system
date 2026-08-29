import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashbaord
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if 'teacher_data' in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data['name']} """)

def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False

def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashbaord()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()
                
    st.header('Login using Password', text_alignment='center')
    st.space()
    st.space()
    teacher_username = st.text_input('Enter username', placeholder='Enter username')
    teacher_password = st.text_input('Enter password', type='password', placeholder='Enter password')

    st.markdown("""
        <hr style='border: none; border-top: 2px solid grey; margin: 20px 0;'>
    """,unsafe_allow_html=True)

    btnc1, btnc2 = st.columns(2)
    with btnc1:
        if st.button('Login', icon=':material/passkey:', shortcut='control+Enter', width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Welcome back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button('Register Instead', type='primary', icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'register'
    
    footer_dashboard()
    

def register_teacher(teacher_username, teacher_name, teacher_password, teacher_confirm_pass):
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_password != teacher_confirm_pass:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Successfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashbaord()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Register your teacher Profile')
    st.space()
    st.space()
    teacher_username = st.text_input('Enter username', placeholder='Enter username')
    teacher_name = st.text_input('Enter name', placeholder='Enter name')
    teacher_password = st.text_input('Enter password', type='password', placeholder='Enter password')
    teacher_confirm_pass = st.text_input('Confirm your password', type='password', placeholder='Enter password')
    
    st.markdown("""
        <hr style='border: none; border-top: 2px solid grey; margin: 20px 0;'>
    """,unsafe_allow_html=True)
    
    btnc1, btnc2 = st.columns(2)
    with btnc1:
        if st.button('Register now', icon=':material/passkey:', shortcut='control+Enter', width='stretch'):
            success, message = register_teacher(teacher_username,  teacher_name, teacher_password, teacher_confirm_pass)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)


    with btnc2:
        if st.button('Login Instead', type='primary', icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'login'
        
    footer_dashboard()
    