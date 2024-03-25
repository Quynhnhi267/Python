f = open("2322024/file/data.txt","r")
print("Tên của file là:",f.name)
print("File có đóng hoặc không? :", f.closed)
print("Chế độ mở file:", f.mode)

line1=f.readline()
line2=f.readline()

print("Dong 1:", line1)
print("Dong 2:", line2)

f.close()