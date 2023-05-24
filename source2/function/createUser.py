from builtins import list
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

def createUser():
    link_avatar = request.headers.get('link_avatar')
    device_name_register = request.headers.get("device_name_register")
    password=request.headers.get("password")

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

        mycursor.execute(f"SELECT MAX(id_user) from user")
        result_id_like = mycursor.fetchall()
        print(result_id_like)
        time_online = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        thong_tin["time online"]=time_online
        thong_tin["link_avatar"]=link_avatar
        thong_tin["password"]=password
        thong_tin["ip_register"]=dia_chi_ip
        thong_tin["device_name_register"]=device_name_register
        thong_tin["operating time"]=0
        sql = f"INSERT INTO user VALUES ({result_id_like[0][0]+1}, %s , %s, %s , %s , %s ,0)"
        val = ( link_avatar,dia_chi_ip,device_name_register , password, time_online)
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
