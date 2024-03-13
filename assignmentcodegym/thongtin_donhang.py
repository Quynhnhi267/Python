# số tiền đã chi
so_tien_chi = int(input("Nhập số tiền bạn đã chi tại cửa hàng: "))

# khởi tạo biến
tien_giam_gia = 0

# các mức ưu đãi
if so_tien_chi < 75:
    print("Bạn không được giảm giá.")
elif so_tien_chi >= 75 and so_tien_chi < 100:
    tien_giam_gia = 15
    print("Bạn được giảm giá 15$.")
elif so_tien_chi >= 100 and so_tien_chi < 150:
    tien_giam_gia = 25
    print("Bạn được giảm giá 25$.")
else:
    tien_giam_gia = 50
    print("Bạn được giảm giá 50$.")
so_tien_thanh_toan = so_tien_chi - tien_giam_gia
print("Số tiền bạn cần thanh toán là:", so_tien_thanh_toan, "$")