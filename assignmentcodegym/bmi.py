# Nhập cân nặng và chiều cao
can_nang = float(input("Nhập cân nặng của bạn: "))
chieu_cao = float(input("Nhập chiều cao của bạn: "))

# Tính BMI
bmi = can_nang / (chieu_cao * chieu_cao)

#Tình trạng cơ thể
tinh_trang_co_the = ""
if bmi < 16:
    tinh_trang_co_the = "Gầy cấp độ III"
elif bmi >= 16 and bmi < 17:
    tinh_trang_co_the = "Gầy cấp độ II"
elif bmi >= 17 and bmi < 18.5:
    tinh_trang_co_the = "Gầy cấp độ I"
elif bmi >= 18.5 and bmi < 25:
    tinh_trang_co_the = "Bình thường"
elif bmi >= 25 and bmi < 30:
    tinh_trang_co_the = "Thừa cân"
elif bmi >= 30 and bmi < 35:
    tinh_trang_co_the = "Béo phì cấp độ I"
elif bmi >= 35 and bmi < 40:
    tinh_trang_co_the = "Béo phì cấp độ II"
else:
    tinh_trang_co_the = "Béo phì cấp độ III"

print("Chỉ số BMI của bạn là:", bmi)
print("Tình trạng cơ thể của bạn là:", tinh_trang_co_the)