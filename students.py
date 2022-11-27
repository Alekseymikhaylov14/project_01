import sqlite3

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_school_name(school_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM School WHERE School_Id = ?"""
        cursor.execute(select_query, (school_id,))
        record = cursor.fetchone()
        close_connection(connection)
        return record[1] 
    except(Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных по школе ", error)
    
def get_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """SELECT * FROM Students WHERE Student_Id = ?"""
        cursor.execute(select_query, (student_id,))
        records = cursor.fetchall()
        for row in records:
            print ("ID студента", row[0])
            print ("Имя студента", row[1])
            print ("ID школы", row[2])
            print ("Название школы", get_school_name(row[2]))
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print ("Ошибка в получении данных ", error)
get_student(202)
