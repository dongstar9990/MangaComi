# Đường dẫn đến file văn bản
file_path = '/home/leoo/PycharmProjects/mangaComi/source2/datasimple.sql'

# Đọc nội dung của file
with open(file_path, 'r') as file:
    content = file.read()

# Hiển thị nội dung ban đầu
print('Nội dung ban đầu:')
print(content)

# Chỉnh sửa nội dung
modified_content = content.replace('"', '')

# Ghi nội dung đã chỉnh sửa vào file
with open(file_path, 'w') as file:
    file.write(modified_content)

# Hiển thị nội dung sau khi đã chỉnh sửa
print('Nội dung sau khi đã chỉnh sửa:')
print(modified_content)