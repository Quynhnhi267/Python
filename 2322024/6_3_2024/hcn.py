class   HCN:
    chieu_dai = 0
    chieu_rong = 0
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def tinh_chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)
 #Khởi tạo đối tượng HCN 1    
hcn_1 = HCN()
hcn_1.chieu_dai = 4
hcn_1.chieu_rong = 5
dien_tich = hcn_1.tinh_dien_tich()
chu_vi = hcn_1.tinh_chu_vi()

print("Diện tích HCN 1:", dien_tich)
print("Chu vi HCN 1:", chu_vi)

#Khởi tạo đối tượng HCN 2
hcn_2 = HCN()
hcn_2.chieu_dai = 6
hcn_2.chieu_rong = 8
dien_tich = hcn_2.tinh_dien_tich()
chu_vi = hcn_2.tinh_chu_vi()

print("Diện tích HCN 2:",dien_tich)
print("Chu vi HCN 2:",chu_vi)
