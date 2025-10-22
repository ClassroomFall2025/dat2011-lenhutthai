class TaiKhoan:
    def __init__(self, soTaiKhoan, ten, loai, soDu=0):
        # Khởi tạo các thuộc tính cơ bản của tài khoản
        self.soTaiKhoan = soTaiKhoan
        self.ten = ten
        self.loai = loai
        self.soDu = soDu

    def taoTaiKhoan(self):
        # Phương thức tạo tài khoản mới
        self.soTaiKhoan = input("Nhập số tài khoản: ")
        self.ten = input("Nhập tên chủ tài khoản: ")
        self.loai = input("Nhập loại tài khoản ('T', 'C'): ")
        self.soDu = float(input("Nhập số dư ban đầu: "))

    def hienThiTaiKhoan(self):
        # Phương thức hiển thị thông tin tài khoản
        print(f"Số tài khoản: {self.soTaiKhoan}")
        print(f"Tên chủ tài khoản: {self.ten}")
        print(f"Loại tài khoản: {'T' if self.loai == 'T' else 'C'}")
        print(f"Số dư tài khoản: {self.soDu:.2f}")

    def guiTien(self, soTien):
        # Phương thức gửi tiền vào tài khoản
        if soTien > 0:
            self.soDu += soTien
            print(f"Đã gửi {soTien:.2f} vào tài khoản. Số dư hiện tại: {self.soDu:.2f}")
        else:
            print("Số tiền gửi phải lớn hơn 0.")

    def rutTien(self, soTien):
        # Phương thức rút tiền từ tài khoản
        if soTien > 0:
            if self.soDu >= soTien:
                self.soDu -= soTien
                print(f"Đã rút {soTien:.2f} từ tài khoản. Số dư hiện tại: {self.soDu:.2f}")
            else:
                print("Số dư không đủ để rút.")
        else:
            print("Số tiền rút phải lớn hơn 0.")

    def toDict(self):
        # Phương thức chuyển đổi tài khoản thành dictionary
        return {
            "soTaiKhoan": self.soTaiKhoan,
            "ten": self.ten,
            "loai": self.loai,
            "soDu": self.soDu
        }

# Sử dụng lớp TaiKhoan
# Tạo một tài khoản mới
taiKhoan1 = TaiKhoan("", "", "", 0)
taiKhoan1.taoTaiKhoan()  # Tạo tài khoản từ đầu vào

# Hiển thị thông tin tài khoản
taiKhoan1.hienThiTaiKhoan()

# Gửi tiền vào tài khoản
taiKhoan1.guiTien(500)

# Rút tiền từ tài khoản
taiKhoan1.rutTien(200)

# Chuyển thông tin tài khoản thành dictionary
taiKhoan_dict = taiKhoan1.toDict()
print(taiKhoan_dict)

        
