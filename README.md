# AI Resume' Analyzer (IntelliResume)

IntelliResume is designed to assist users in enhancing their resumes by leveraging artificial intelligence. It analyzes resumes, provides insights into skills, recommendations for improvement, and suggestions for enhancing the overall quality of the resume.




## Features

**Resume Parsing:** Extracts key information from uploaded resumes, including skills, experience, education, and contact details.


**Resume Scoring:** Provides a score or evaluation based on the content and structure of the resume.


**Skill Recommendations:** Recommends additional skills based on the user's current skill set.

**Course Recommendations:** Suggests relevant courses to improve skills or fill gaps.

**User Level Assessment:** Analyzes the experience level of the user based on the resume content.


## Technologies Used

**Python:** The primary programming language used for development.
**Streamlit:** Utilized for creating the user interface and frontend.
**PyResparser:** Handles the extraction of data from resumes.
**Pandas, Plotly Express:** Used for data manipulation and visualization.
**Spacy, NLTK:** Provides natural language processing capabilities.

## Run Locally

Clone the project

```bash
  git clone git@github.com:sallar-ba/IntelliResume.git
```

Go to the project directory

```bash
  cd IntelliResume
```

Create Virtual Environment

```
  python -m venv venv
```
Activate
```
  venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create DB
```
    mysql -u your_username -p
    CREATE DATABASE resumedb;
```

Update username and password in __init__.py

Start the app
```bash
  streamlit run main.py
```



## Usage

1. **User Mode:** Upload your resume to receive smart recommendations, skill insights, and a score.
2. **Admin Mode:** Admins can log in to access a dashboard displaying user data and insights based on the collected data.

