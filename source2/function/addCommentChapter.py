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

def addCommentChapter():
    id_user = request.headers.get('id_user')
    link_chapter = request.headers.get('link_chapter')
    link_manga = request.headers.get('link_manga')
    device_comment = request.headers.get("device_comment")
    noidungComment = request.headers.get('noidungComment')
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

        mycursor.execute(f"SELECT MAX(id_comment) from comment_chapter")
        result_id_like = mycursor.fetchall()
        print(result_id_like)
        date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        thong_tin["id_user"]=id_user
        thong_tin["dateTimeComment"]=date
        thong_tin["link_chapter"]=link_chapter
        thong_tin["link_manga"]=link_manga
        thong_tin["ip_comment"]=dia_chi_ip
        thong_tin["device_comment"]=device_comment
        sql = f"INSERT INTO comment_chapter VALUES ( {result_id_like[0][0] +1 } , %s , %s , %s , %s  , {id_user},%s)"
        val = (link_chapter,link_manga , dia_chi_ip,device_comment , noidungComment)
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
