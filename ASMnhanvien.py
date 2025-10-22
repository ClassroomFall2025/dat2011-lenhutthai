# Tạo lớp NhanVien
class NhanVien:
    def __init__(self, ma, ho_ten, luong):
        self.ma = str(ma).strip()
        self.ho_ten = str(ho_ten).strip()
        try:
            self.luong = float(luong)
        except:
            self.luong = 0

    def get_thunhap(self):
        return self.luong

    def get_thue(self):
        thunhap = self.get_thunhap()
        if thunhap < 9000000:
            return 0
        elif thunhap <= 15000000:
            return thunhap * 0.1
        else:
            return thunhap * 0.12

    def to_dict(self):
        return {
            "type": "NV",
            "ma": self.ma,
            "ho_ten": self.ho_ten,
            "luong": f"{self.luong:.2f}",
            "doanh_so": "",
            "ty_le": "",
            "luong_trach_nhiem": ""
        }
    
    @staticmethod
    def from_dict(d):
        return NhanVien(d.get("ma",""), d.get("ho_ten",""), float(d.get("luong") or 0))

    def __str__(self):
        return f"{self.ma} | {self.ho_ten} | Lương: {self.luong:.0f} | Thu nhập: {self.get_thunhap():.0f} | Thuế: {self.get_thue():.0f}"

# Tạo lớp TiepThi kế thừa từ NhanVien
class TiepThi(NhanVien):
    def __init__(self, ma, ho_ten, luong, doanh_so, ty_le):
        super().__init__(ma, ho_ten, luong)
        try:
            self.doanh_so = float(doanh_so)
        except:
            self.doanh_so = 0
        try:
            self.ty_le = float(ty_le)
        except:
            self.ty_le = 0

    def get_thunhap(self):
        hoa_hong = self.doanh_so * (self.ty_le / 100)
        return self.luong + hoa_hong

    def to_dict(self):
        return {
            "type": "TT",
            "ma": self.ma,
            "ho_ten": self.ho_ten,
            "luong": f"{self.luong:.2f}",
            "doanh_so": f"{self.doanh_so:.2f}",
            "ty_le": f"{self.ty_le:.2f}",
            "luong_trach_nhiem": ""
        }

    @staticmethod
    def from_dict(d):
        return TiepThi(d.get("ma",""), d.get("ho_ten",""), d.get("luong") or 0, d.get("doanh_so") or 0, d.get("ty_le") or 0)

    def __str__(self):
        return (f"{self.ma} | {self.ho_ten} | Tiếp thị | Lương: {self.luong:.0f} | "
                f"Doanh số: {self.doanh_so:.0f} | TL%: {self.ty_le:.1f}% | "
                f"Thu nhập: {self.get_thunhap():.0f} | Thuế: {self.get_thue():.0f}")

# Tạo lớp TruongPhong kế thừa từ NhanVien
class TruongPhong(NhanVien):
    def __init__(self, ma, ho_ten, luong, luong_trach_nhiem):
        super().__init__(ma, ho_ten, luong)
        try:
            self.luong_trach_nhiem = float(luong_trach_nhiem)
        except:
            self.luong_trach_nhiem = 0.0

    def get_thunhap(self):
        return self.luong + self.luong_trach_nhiem

    def to_dict(self):
        return {
            "type": "TP",
            "ma": self.ma,
            "ho_ten": self.ho_ten,
            "luong": f"{self.luong:.2f}",
            "doanh_so": "",
            "ty_le": "",
            "luong_trach_nhiem": f"{self.luong_trach_nhiem:.2f}"
        }

    @staticmethod
    def from_dict(d):
        return TruongPhong(d.get("ma",""), d.get("ho_ten",""), d.get("luong") or 0, d.get("luong_trach_nhiem") or 0)

    def __str__(self):
        return (f"{self.ma} | {self.ho_ten} | Trưởng phòng | Lương: {self.luong:.0f} | "
                f"Lương TN: {self.luong_trach_nhiem:.0f} | Thu nhập: {self.get_thunhap():.0f} | Thuế: {self.get_thue():.0f}")
