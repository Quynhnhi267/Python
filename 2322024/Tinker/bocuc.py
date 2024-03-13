# Khai báo  
from tkinter import *
from tkinter import ttk
#Tạo cửa sổ
root = Tk()
# Thiết lập độ rộng
root.geometry("400x250")
root.configure(bg="green")
# Đặt tiêu đề cho cửa sổ chính
root.title("First_Program")

# Phần thân chương trình
Button(root, text= "Red", fg = "red").pack(side= LEFT)
Button(root, text= "Pink", fg = "pink").pack(side= RIGHT) 
Button(root, text= "Yellow", fg = "yellow").pack(side= TOP)
Button(root, text= "Blue", fg = "blue").pack(side= BOTTOM)
root.mainloop()