class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh
    def get_diem(self):
        pass
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            return "Xuất sắc"
        elif self.get_diem() >= 8 and self.get_diem() < 9:
            return "Giỏi"
        elif self.get_diem() >= 7 and self.get_diem() < 8:
            return "Khá"
        elif self.get_diem() >= 5 and self.get_diem() < 7:
            return "Trung bình"
        else:
            return "Yếu"
    def xuat(self):
        print(f'Họ tên: {self.ho_ten} Ngành: {self.nganh} Học lực: {self.get_hoc_luc()}')
    def __str__(self):
        return f'{self.ho_ten} {self.nganh} {self.get_hoc_luc()}'

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, nganh)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css
    def get_diem(self):
        return (self.diem_java * 2 + self.diem_html + self.diem_css) / 4

class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh)
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales
    def get_diem(self):
        return (self.diem_marketing * 2 + self.diem_sales) / 3