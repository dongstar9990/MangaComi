from datetime import datetime
from flask import request
import mysql.connector


def checkOnline(iduser):
    thong_tin = {}
    list_thong_tin = []
    flag=""
    config = {
        'user': 'leooRealman',
        'password': 'BAdong14102001!',
        'host': 'localhost',
        'port': 3306,
        'database': 'mangaComivs2'
    }
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()[0]
            print(f"You are connected to database: {db_name}")
        mycursor = connection.cursor()
        mycursor.execute(f"SELECT thoiGianHoatdong from user where id_user={iduser}")
        result_id_readed = mycursor.fetchall()
        print(result_id_readed)
        if(result_id_readed[0][0]=="None"):
            flag="not online"
        else:
            flag="online"
    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
    return flag
