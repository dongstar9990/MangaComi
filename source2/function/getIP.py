import  socket
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