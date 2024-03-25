from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Chương trình máy tính")
# Phần thân chương trình
def addNumbers():
    Name1 = float(Kg.get())
    gram = Name1 * 1000
    pound = Name1 * 2.20462
    ounce = Name1 * 35.274

Label(root,text="Gram").grid(row=1,column=0)
gram  = Entry(root)
gram.grid(row=2, column=0)

Label(root,text="Pounds").grid(row=1,column=1)
pounds  = Entry(root)
pounds.grid(row=2, column=1)

Label(root,text="Ounce").grid(row=1,column=2)
ounce  = Entry(root)
ounce.grid(row=2, column=2)

Label(root,text="Enter the weight in Kg").grid(row=0, column=0)
Kg = Entry(root)
Kg.grid(row=0, column=1)


Button(root,text="Convert",command=addNumbers).grid(row=0, column=2)
ket_qua = Label(root,text="")
ket_qua.grid(row=2, column=1)
root.mainloop()












import tkinter as tk

def convert_weight():
    kg = float(e2_value.get())
    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274

    e3.delete("1.0", END)
    e3.insert(END, gram)

    e4.delete("1.0", END)
    e4.insert(END, pound)

    e5.delete("1.0", END)
    e5.insert(END, ounce)

# Khởi tạo cửa sổ
window = tk.Tk()
window.title("Chuyển đổi cân nặng")

# Khởi tạo GUI
e1 = tk.Label(text="Nhập cân nặng (Kg): ")
e2_value = tk.StringVar()
e2 = tk.Entry(textvariable=e2_value)
b1 = tk.Button(text="Chuyển đổi", command=convert_weight)
e3 = tk.Label(text="Gram: ")
e4 = tk.Label(text="Pounds: ")
e5 = tk.Label(text="Ounce: ")
e6 = tk.Text(height=1, width=20)
e7 = tk.Text(height=1, width=20)
e8 = tk.Text(height=1, width=20)

# Chia vị trí các cột giá trị
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
b1.grid(row=0, column=2)
e3.grid(row=1, column=0)
e6.grid(row=1, column=1)
e4.grid(row=2, column=0)
e7.grid(row=2, column=1)
e5.grid(row=3, column=0)
e8.grid(row=3, column=1)

# Gọi vòng lặp sự kiện chính
window.mainloop()