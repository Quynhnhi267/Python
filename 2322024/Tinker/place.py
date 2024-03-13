# Khai báo  
from tkinter import *
from tkinter import ttk
#Tạo cửa sổ
root = Tk()
# Thiết lập độ rộng
root.geometry("400x250")
root.configure(bg="green")
# Đặt tiêu đề cho cửa sổ chính
root.title("Bố cục với Place")
# Phần thân chương trình
Label(root,text="Name").place(x= 30,y=50)
Label(root,text="Email").place(x=30,y=90)
Label(root,text="Password").place(x=95,y=130)
root.mainloop()