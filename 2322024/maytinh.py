def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
a = int(input("Nhap vao so thu nhat: "))
b = int(input("Nhap vao so thu hai: "))
option = input("Nhap phep toan: ")
if option == "+":
    print(a,"+",b,"=",add(a,b))
elif option == "-":
    print(a,"-",b,"=",subtract(a,b))
elif option == "*":
    print(a,"*",b,"=",multiply(a,b))
elif option == "/":
    print(a,"/",b,"=",divide(a,b))
else:
    print("Gia tri khong hop le")