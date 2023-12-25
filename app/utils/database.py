import pymysql


connection = pymysql.connect(host='localhost',user='root',password='6117',db='resumedb', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()




def create_db():
    db_sql = """CREATE DATABASE IF NOT EXISTS ResumeDB;"""
    cursor.execute(db_sql)

def create_table():
    DB_table_name = 'user_data'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     Name varchar(500) NOT NULL,
                     Email_ID VARCHAR(500) NOT NULL,
                     resume_score VARCHAR(8) NOT NULL,
                     Timestamp VARCHAR(50) NOT NULL,
                     Page_no VARCHAR(5) NOT NULL,
                     Predicted_Field BLOB NOT NULL,
                     User_level BLOB NOT NULL,
                     Actual_skills BLOB NOT NULL,
                     Recommended_skills BLOB NOT NULL,
                     Recommended_courses BLOB NOT NULL,
                     PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)

def create_admin_table():
    DB_table_name = 'admin_data'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     Username varchar(500) NOT NULL,
                     Password VARCHAR(500) NOT NULL,
                     PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)

def add_admin(username, password):
    cursor.execute("INSERT INTO admin_data (Username, Password) VALUES (%s, %s)", (username, password))
    connection.commit()

def insert_data(name, email, res_score, timestamp, no_of_pages, reco_field, cand_level, skills, recommended_skills, courses):
    try:
        DB_table_name = 'user_data'
        insert_sql = "INSERT INTO " + DB_table_name + " VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        rec_values = (name, email, str(res_score), timestamp, str(no_of_pages), reco_field, cand_level, skills, recommended_skills, courses)

        cursor.execute(insert_sql, rec_values)
        connection.commit()
    except Exception as e:
        print(f"Error inserting data: {str(e)}")

