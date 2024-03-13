import may_tinh
a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
option = input("Nhap phep toan: ")
if option == "+":
    print(a,"+",b,"=",may_tinh.add(a,b))
elif option == "-":
    print(a,"-",b,"=",may_tinh.subtract(a,b))
elif option == "*":
    print(a,"*",b,"=",may_tinh.multiply(a,b))
elif option == "/":
    print(a,"/",b,"=",may_tinh.divide(a,b))
else:
    print("Gia tri khong hop le")