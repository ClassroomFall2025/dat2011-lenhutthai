from lab6_sinhvienpoly import *

class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def nhap_sinh_vien(self):
        while True:
            ho_ten = input("Họ tên sinh viên (hoặc nhập 'q' để dừng): ")
            if ho_ten.lower() == 'q':
                break
            nganh = input("Ngành (it/biz): ").strip().lower()
            if nganh == "it":
                diem_java = float(input("Điểm Java: "))
                diem_html = float(input("Điểm HTML: "))
                diem_css = float(input("Điểm CSS: "))
                sv = SinhVienIT(ho_ten, nganh, diem_java, diem_html, diem_css)
                self.dssv.append(sv)
            elif nganh == "biz":
                diem_marketing = float(input("Điểm Marketing: "))
                diem_sales = float(input("Điểm Sales: "))
                sv = SinhVienBiz(ho_ten, nganh, diem_marketing, diem_sales)
                self.dssv.append(sv)
            else:
                print("Ngành không hợp lệ. Vui lòng nhập lại.")
    def xuat_sinh_vien(self):
        for sv in self.dssv:
            sv.xuat()
    def xuat_sinh_vien_gioi(self):
        for sv in self.dssv:
            if sv.get_hoc_luc() in ("Xuat sac", "Gioi"):
                sv.xuat()
    def sap_xep_sinh_vien_theo_diem(self):
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        for i, sv in enumerate(self.dssv, start=1):
            print(f'Tên: {i}. {sv} Điểm: {sv.get_diem():.2f}')
    
    
                
    