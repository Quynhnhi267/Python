file = open("file/data.txt", "r")
print ("Tên của file là: ", file.name)
print ("File có đóng hoặc không? : ", file.closed)
print ("Chế độ mở file : ", file.mode)
str = file.read()
print("Noi dung file: \n",str)
file.close()