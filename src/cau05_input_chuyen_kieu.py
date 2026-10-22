ma_may = input("Nhập mã máy: ")
cong_suat_str = input("Nhập công suất (W): ")
so_phut_str = input("Nhập số phút sử dụng: ")
don_gia_str = input("Nhập đơn giá điện/kWh: ")

print("\n--- Kiểu dữ liệu ngay sau khi nhập bằng input() ---")
print("Mã máy:", ma_may, "- Kiểu:", type(ma_may))
print("Công suất:", cong_suat_str, "- Kiểu:", type(cong_suat_str))
print("Số phút:", so_phut_str, "- Kiểu:", type(so_phut_str))
print("Đơn giá:", don_gia_str, "- Kiểu:", type(don_gia_str))

cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

print("\n--- Kiểu dữ liệu sau khi chuyển đổi kiểu ---")
print("Công suất:", cong_suat_w, "- Kiểu:", type(cong_suat_w))
print("Số phút:", so_phut, "- Kiểu:", type(so_phut))
print("Đơn giá:", don_gia_kwh, "- Kiểu:", type(don_gia_kwh))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả tính toán ---")
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí điện (VNĐ):", chi_phi)