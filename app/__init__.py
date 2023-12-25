import streamlit as st
import pandas as pd
import time, datetime


from pyresparser import ResumeParser



from streamlit_tags import st_tags
from PIL import Image


import plotly.express as px
import nltk
import spacy

import os

from app.utils.pdf_utils import show_pdf
from app.utils.helper import get_table_download_link, recommendation, candidate_level, score, recommend_vids, show_user_data
from app.utils.database import insert_data, create_db, create_table, connection, cursor, create_admin_table, add_admin


os.environ["PAFY_BACKEND"] = "internal"

nlp = spacy.load("en_core_web_sm")


st.set_page_config(
   page_title="IntelliResume",
   page_icon='app/imgs/logo2.png',
)


def run():
    img = Image.open('app/imgs/logo1.png')
    st.image(img)

    # SIDEBAR
    st.sidebar.markdown("# Choose Role")
    activities = ["User", "Admin"]
    choice = st.sidebar.selectbox("", activities)
    link = '[© Developed by Sallar ](https://www.linkedin.com/in/sallar-ba/)'
    st.sidebar.markdown(link, unsafe_allow_html=True)
    # ------------------------------ #
    
    if choice == 'User':
        st.markdown('''<h5 style='text-align: left; color: #4169E1;'> Upload Your Resume and Let the AI Magic Give you Smart Recommendations</h5>''',
                    unsafe_allow_html=True)
        pdf_file = st.file_uploader("", type=["pdf"])
        if pdf_file is not None:
            with st.spinner('Uploading your Resume...'):
                time.sleep(4)
            save_image_path = 'app/Uploaded_Resumes/'+pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            show_pdf(save_image_path)
            resume_data = ResumeParser(save_image_path).get_extracted_data()
            if resume_data:
                resume_text = show_user_data(resume_data, save_image_path)

                # DATABASE INITIALIZATION
                create_db()
                create_table()

                #### CANIDATE LEVEL
                cand_level = candidate_level(resume_data)

                ## Skill shows
                st_tags(label='### Your Current Skills',
                text='See our skills recommendation below',
                    value=resume_data['skills'],key = '1  ')

                # RECOMMENDED SKILLS
                recommended_skills,reco_field,rec_course = recommendation(resume_data)
                
                ## Getting Curr Time
                ts = time.time()
                cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                timestamp = str(cur_date+'_'+cur_time)

                ### Resume writing recommendation
                st.subheader("**Resume Tips & Ideas💡**")
                
                # RESUME SCORE
                resume_score = score(resume_text)

                # Insert into database
                insert_data(resume_data['name'], resume_data['email'], str(resume_score), timestamp,
                              str(resume_data['no_of_pages']), reco_field, cand_level, str(resume_data['skills']),
                              str(recommended_skills), str(rec_course))


                # RECOMMNEDED COURSES
                recommend_vids()

            else:
                st.error('Something went wrong..')
    else:
        ## Admin Side
        st.success('Welcome to Admin Side')

        create_db()
        create_table()
        create_admin_table()
        
        options = ["Login", "Signup"]
        choice = st.radio("Choose an option", options)

        if choice == "Signup":
            new_user = st.text_input("New Username")
            new_password = st.text_input("New Password", type='password')
            confirm_password = st.text_input("Confirm Password", type='password')

            if st.button('Sign Up'):
                if new_password == confirm_password:
                    add_admin(new_user, new_password)
                    st.success("Signup successful! Now you can login.")
                else:
                    st.error("Passwords don't match. Try again.")

        elif choice == "Login":
            ad_user = st.text_input("Username")
            ad_password = st.text_input("Password", type='password')

            if st.button('Login'):
                cursor.execute("SELECT * FROM admin_data WHERE Username=%s AND Password=%s", (ad_user, ad_password))
                result = cursor.fetchone()
            
                if result:
                    st.success(f"Welcome {ad_user}!")
                
                    # Display Data
                    cursor.execute('''SELECT * FROM user_data''')
                    data = cursor.fetchall()
                    st.header("**User's Data**")
                    df = pd.DataFrame(data)
                    st.dataframe(df)
                    st.markdown(get_table_download_link(df,'User_Data.csv','Download Report'), unsafe_allow_html=True)
                    






            else:
                st.error("Invalid username or password")
