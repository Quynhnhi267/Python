f = open("2322024/file/data.txt","a+")
f.write("\nNguyen Quynh Nhi")
f.close()
f = open("2322024/file/data.txt","r+")
line1=f.readline()
line2=f.readline()
line3=f.readline()

print("Dong 1:", line1)
print("Dong 2:", line2)
print("Dong 3:", line3)
f.close()
