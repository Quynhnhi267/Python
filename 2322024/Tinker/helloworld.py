# Khai báo  
from tkinter import *
from tkinter import ttk
#Tạo cửa sổ
root = Tk()
# Thiết lập độ rộng
root.geometry("400x250")
# Đặt tiêu đề cho cửa sổ chính
root.title("First_Program")

# Phần thân chương trình
Button(root, text= "Red", fg = "red").pack(side= LEFT)
Button(root, text= "Pink", fg = "pink").pack(side= RIGHT) 
Button(root, text= "Yellow", fg = "yellow").pack(side= TOP)
Button(root, text= "Blue", fg = "blue").pack(side= BOTTOM)
Label(root,text="Hello World !").pack()
#Tạo nút nhấn
ttk.Button(root, text="Cộng").pack()
#Select box
ttk.Combobox(root, values=["Mùa xuân","Mùa hạ","Mùa thu","Mùa đông"]).pack()
#Check box
ttk.Checkbutton(root, text="Chọn").pack()
#Ô nhập dữ liệu
ttk.Entry(root).pack()
# Thanh kéo
ttk.Scale(root, from_=0, to=100, orient= HORIZONTAL).pack()
# Ô nhập số
ttk.Spinbox(root, from_=0, to=100).pack()
# Ô nhập nhiều text
Text(root).pack()
root.mainloop()