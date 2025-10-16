import html
from ctypes import c_ssize_t
from platform import java_ver
class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh
    def get_diem():
        pass
    def get_hoc_luc(self):
        if self.get_diem >= 9 and self.get_diem <= 10:
            return "Xuat sac"
        elif self.get_diem() >= 8 and self.get_diem() < 9:
            return "Gioi"
        elif self.get_diem >= 7 and self.get_diem < 8:
            return "Kha"
        elif self.get_diem >= 5 and self.get_diem < 7:
            return "Trung binh"
        else:
            return "Yeu"
    def xuat(self):
        print(f'{self.ho_ten} {self.nganh} {self.get_hoc_luc()}')
    def __str__(self):
        return f'{self.ho_ten} {self.nganh} {self.get_hoc_luc()}'

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh):
        super().__init__(ho_ten, nganh)
        self.java = java
        self.html = html
        self.css = css
    def get_diem(self):
        return (self.jav * 2 + self.html + self.css) / 4

class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, ):
        super().__init__(ho_ten, nganh)