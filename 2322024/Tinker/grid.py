# Khai báo  
from tkinter import *
from tkinter import ttk
#Tạo cửa sổ
root = Tk()
# Thiết lập độ rộng
root.geometry("400x250")
root.configure(bg="green")
# Đặt tiêu đề cho cửa sổ chính
root.title("Bố cục với Grid")
# Phần thân chương trình 
Label(root, text= "Tài khoản").grid(row = 0,column=0)
Entry(root).grid(row=0, column=1)
Label(root,text="Mật khẩu").grid(row=1, column=0)
Entry(root).grid(row=1,column=1)
Button(root,text="Đăng nhập").grid(row=2,column=0)
root.mainloop()