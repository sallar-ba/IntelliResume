import time

import streamlit as st
from streamlit_tags import st_tags


import base64, random

from app.utils.courses import ds_course,web_course,android_course,ios_course,uiux_course, resume_videos,interview_videos
from app.utils.pdf_utils import pdf_reader

def get_table_download_link(df,filename,text):

    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href






def course_recommender(course_list):
    st.subheader("Courses & Certificates Recommendations 🎓")
    c = 0
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 5)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course

def show_user_data(resume_data, save_image_path):
    ## Get the whole resume data
    resume_text = pdf_reader(save_image_path)

    st.header("**Resume Analysis**")
    st.success("Hello "+ resume_data['name'])
    st.subheader("**Your Basic info**")
    try:
        st.text('Name: '+resume_data['name'])
        st.text('Email: ' + resume_data['email'])
        st.text('Contact: ' + resume_data['mobile_number'])
        st.text('Resume pages: '+str(resume_data['no_of_pages']))
    except:
        pass
    return resume_text

def candidate_level(resume_data):
    cand_level = ''
    if resume_data['no_of_pages'] == 1:
        cand_level = "Fresher"
        st.markdown( '''<h4 style='text-align: left; color: #d73b5c;'>You are at Fresher level!</h4>''',unsafe_allow_html=True)
    elif resume_data['no_of_pages'] == 2:
        cand_level = "Intermediate"
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>You are at intermediate level!</h4>''',unsafe_allow_html=True)
    elif resume_data['no_of_pages'] >=3:
        cand_level = "Experienced"
        st.markdown('''<h4 style='text-align: left; color: #fba171;'>You are at experience level!''',unsafe_allow_html=True)

    return cand_level


def recommendation(resume_data):
    ##  keywords
    ds_keyword = ['tensorflow','keras','pytorch','machine learning','deep Learning','flask','streamlit', 'jupyter notebooks','data visualization','predictive analysis','statistical modeling','data mining','clustering & classification','data analytics','quantitative analysis','web scraping','ml algorithms','probability','scikit-learn','data science','pandas','numpy','matplotlib','seaborn','nltk','opencv','beautifulsoup','sql','tableau','power bi','powerpoint','excel','big data','hadoop','spark','hive','aws','azure','google cloud','ibm cloud','python','r','java','c++','c','javascript','html','css','git','github','bitbucket','docker','kubernetes','linux','unix','bash','command line','jira','agile','scrum']
    web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                   'javascript', 'angular js', 'c#', 'flask', 'sdk', 'html', 'css', 'git', 'github']
    android_keyword = ['android','android development','flutter','kotlin','xml','kivy', 'git', 'sdk', 'sqlite']
    ios_keyword = ['ios','ios development','swift','cocoa','cocoa touch','xcode', 'objective-c', 'sqlite', 'plist', 'storekit', 'ui-kit', 'av foundation', 'auto-layout', 'git', 'github']
    uiux_keyword = ['ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes','storyframes','adobe photoshop','photoshop','editing','adobe illustrator','illustrator','adobe after effects','after effects','adobe premier pro','premier pro','adobe indesign','indesign','wireframe','solid','grasp','user research','user experience']

    recommended_skills = []
    reco_field = ''
    rec_course = ''
    ## Courses recommendation
    for i in resume_data['skills']:
        ## Data science recommendation
        if i.lower() in ds_keyword:
            print(i.lower())
            reco_field = 'Data Science'
            st.success("** Our analysis says you are looking for Data Science Jobs.**")
            recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining','Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping','ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
            recommended_keywords = st_tags(label='### Recommended skills for you.',
            text='Recommended skills generated from System',value=recommended_skills,key = '2')
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job</h4>''',unsafe_allow_html=True)
            rec_course = course_recommender(ds_course)
            break

        ## Web development recommendation
        elif i.lower() in web_keyword:
            print(i.lower())
            reco_field = 'Web Development'
            st.success("** Our analysis says you are looking for Web Development Jobs **")
            recommended_skills = ['React','Django','Node JS','React JS','php','laravel','Magento','wordpress','Javascript','Angular JS','c#','Flask','SDK']
            recommended_keywords = st_tags(label='### Recommended skills for you.',
            text='Recommended skills generated from System',value=recommended_skills,key = '3')
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
            rec_course = course_recommender(web_course)
            break

        ## Android App Development
        elif i.lower() in android_keyword:
            print(i.lower())
            reco_field = 'Android Development'
            st.success("** Our analysis says you are looking for Android App Development Jobs **")
            recommended_skills = ['Android','Android development','Flutter','Kotlin','XML','Java','Kivy','GIT','SDK','SQLite']
            recommended_keywords = st_tags(label='### Recommended skills for you.',
            text='Recommended skills generated from System',value=recommended_skills,key = '4')
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
            rec_course = course_recommender(android_course)
            break

        ## IOS App Development
        elif i.lower() in ios_keyword:
            print(i.lower())
            reco_field = 'IOS Development'
            st.success("** Our analysis says you are looking for IOS App Development Jobs **")
            recommended_skills = ['IOS','IOS Development','Swift','Cocoa','Cocoa Touch','Xcode','Objective-C','SQLite','Plist','StoreKit',"UI-Kit",'AV Foundation','Auto-Layout']
            recommended_keywords = st_tags(label='### Recommended skills for you.',
            text='Recommended skills generated from System',value=recommended_skills,key = '5')
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
            rec_course = course_recommender(ios_course)
            break

        ## Ui-UX Recommendation
        elif i.lower() in uiux_keyword:
            print(i.lower())
            reco_field = 'UI-UX Development'
            st.success("** Our analysis says you are looking for UI-UX Development Jobs **")
            recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
            recommended_keywords = st_tags(label='### Recommended skills for you.',
            text='Recommended skills generated from System',value=recommended_skills,key = '6')
            st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
            rec_course = course_recommender(uiux_course)
            break
    return recommended_skills,reco_field,rec_course


def score(resume_text):
    resume_score = 0
    if 'Objective' in resume_text:
        resume_score = resume_score+20
        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Objective</h4>''',unsafe_allow_html=True)
    else:
        st.markdown('''<h5 style='text-align: left; color: #ff0000;'>[-] Please add your career objective, it will give your career intension to the Recruiters.</h4>''',unsafe_allow_html=True)

    if 'Declaration'  in resume_text:
        resume_score = resume_score + 20
        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added Delcaration/h4>''',unsafe_allow_html=True)
    else:
        st.markdown('''<h5 style='text-align: left; color: #ff0000;'>[-] Please add Declaration. It will give the assurance that everything written on your resume is true and fully acknowledged by you</h4>''',unsafe_allow_html=True)

    if 'Hobbies' or 'Interests'in resume_text:
        resume_score = resume_score + 20
        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Hobbies</h4>''',unsafe_allow_html=True)
    else:
        st.markdown('''<h5 style='text-align: left; color: #ff0000;'>[-] Please add Hobbies. It will show your persnality to the Recruiters and give the assurance that you are fit for this role or not.</h4>''',unsafe_allow_html=True)

    if 'Achievements' in resume_text:
        resume_score = resume_score + 20
        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Achievements </h4>''',unsafe_allow_html=True)
    else:
        st.markdown('''<h5 style='text-align: left; color: #ff0000;'>[-] Please add Achievements. It will show that you are capable for the required position.</h4>''',unsafe_allow_html=True)

    if 'Projects' in resume_text:
        resume_score = resume_score + 20
        st.markdown('''<h5 style='text-align: left; color: #1ed760;'>[+] Awesome! You have added your Projects</h4>''',unsafe_allow_html=True)
    else:
        st.markdown('''<h5 style='text-align: left; color: #ff0000;'>[-] Please add Projects. It will show that you have done work related the required position or not.</h4>''',unsafe_allow_html=True)

    st.subheader("**Resume Score📝**")
    st.markdown(
        """
        <style>
            .stProgress > div > div > div > div {
                background-color: #d73b5c;
            }
        </style>""",
        unsafe_allow_html=True,
    )
    my_bar = st.progress(0)
    score = 0
    for percent_complete in range(resume_score):
        score +=1
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    st.success(f'Your Resume Writing Score: {str(score)}')
    st.warning("Note: This score is calculated based on the content that you have in your Resume.")

    return score

def recommend_vids():
    ## Resume writing video
    st.header("**Bonus Video for Resume Writing Tips💡**")
    resume_vid = random.choice(resume_videos)
    st.video(resume_vid)

                ## Interview Preparation Video
    st.header("**Bonus Video for Interview Tips💡**")
    interview_vid = random.choice(interview_videos)
    st.video(interview_vid)