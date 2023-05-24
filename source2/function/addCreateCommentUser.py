from datetime import datetime
from flask import request
import mysql.connector
import socket

def get_ip_address():
    # Lấy tên máy chủ của máy tính hiện tại
    hostname = socket.gethostname()

    # Lấy địa chỉ IP tương ứng với tên máy chủ
    ip_address = socket.gethostbyname(hostname)

    return ip_address

def get_api_ip(api_url):
    try:
        ip = socket.gethostbyname(api_url)
        return ip
    except socket.gaierror:
        return None

def addCommentUser():
    id_user = request.headers.get('id_user')
    Id_User_Bi_Comment = request.headers.get('Id_User_Bi_Comment')
    Id_User_Comment = request.headers.get('Id_User_Comment')
    NoiDungComment = request.headers.get('NoiDungComment')
    link_image_attach = request.headers.get("link_image_attach")
    nameDevice_Comment = request.headers.get('nameDevice_Comment')
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

        dia_chi_ip = get_ip_address()

        mycursor.execute(f"SELECT MAX(idComment_tt) from comment_user")
        result_id_like = mycursor.fetchall()
        print(result_id_like)
        date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        thong_tin["id_user"]=id_user
        thong_tin["dateTimeComment"]=date
        thong_tin["NoiDungComment"]=NoiDungComment
        thong_tin["link_image_attach"]=link_image_attach
        thong_tin["nameDevice_Comment"]=nameDevice_Comment
        sql = f"INSERT INTO comment_user VALUES ( {Id_User_Bi_Comment},{Id_User_Comment},{result_id_like[0][0]+1}, %s , %s , %s , %s  ,%s)"
        val = (NoiDungComment,link_image_attach , date,nameDevice_Comment , dia_chi_ip)
        mycursor.execute(sql, val)
        result1 = mycursor.fetchall()

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
    return thong_tin
