from datetime import datetime
from flask import request
import mysql.connector


def List200commentChapter():
    thong_tin = {}
    list_thong_tin = []
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


        mycursor.execute(f"SELECT * from comment_chapter ORDER BY id_comment DESC LIMIT 200 ")
        result_id_readed = mycursor.fetchall()
        print(result_id_readed)
        for i in range(0 , 4):
            thong_tin["idComment"] = result_id_readed[i][0]
            thong_tin["link_chapter"] = result_id_readed[i][1]
            thong_tin["link_manga"] = result_id_readed[i][2]
            thong_tin["ip_comment"] = result_id_readed[i][3]
            thong_tin["device_comment"] = result_id_readed[i][4]
            thong_tin["noidungComment"] = result_id_readed[i][5]
            list_thong_tin.append(thong_tin)
            thong_tin = {}
        # luu cac thay doi vao trong database
        connection.commit()
        # mycursor.execute("SELECT thong_tin from skhanhphuc")
        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL database: {error}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")
    return list_thong_tin