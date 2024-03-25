# Khai báo  
from tkinter import *
from tkinter import ttk
#Tạo cửa sổ
root = Tk()
# Thiết lập độ rộng
root.geometry("400x250")
root.configure(bg="green")
# Đặt tiêu đề cho cửa sổ chính
root.title("Họ và tên")
# Phần thân chương trình
def addNumbers():
    Name1 = Ho.get()
    Name2 = Ten.get()
    result =Name1 + " "+Name2
    ket_qua.config(text="Xin chào"+ result)

Label(root,text="Họ").grid(row=0, column=0)
Ho = Entry(root)
Ho.grid(row=0, column=1)


Label(root,text="Tên").grid(row=1, column=0)
Ten = Entry(root)
Ten.grid(row=1, column=1)

Button(root,text="Họ va tên",command=addNumbers).grid(row=2, column=0)
ket_qua = Label(root,text="Xin chào")
ket_qua.grid(row=2, column=1)
root.mainloop()