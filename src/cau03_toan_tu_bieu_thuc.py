tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print("Số giờ trọn vẹn:", so_gio)
print("Số phút còn lại:", so_phut_con_lai)

su_dung_lau = tong_phut > 60
print("Sử dụng lâu (> 60 phút):", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

ket_qua_1 = 100 + 20 * 3
ket_qua_2 = (100 + 20) * 3
print("Kết quả 100 + 20 * 3 =", ket_qua_1)
print("Kết quả (100 + 20) * 3 =", ket_qua_2)