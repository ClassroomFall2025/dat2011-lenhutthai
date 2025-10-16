class SanPham:
    def __init__(self, ten, gia, giam_gia):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia
    # phuong thuc nhap
    def nhap_thong_tin(self):
        self.__ten = input('Nhập tên sản phẩm: ')
        self.__gia = float(input('Nhập giá sản phẩm: '))
        self.__giam_gia = float(input('Nhập giảm giá sản phẩm (%): '))
    # phuong thuc xuat
    def xuat_thong_tin(self):
        print(f'Tên sản phẩm: {self.__ten}')
        print(f'Giá: {self.__gia}')
        print(f'Giảm giá: {self.__giam_gia}')
    # phuong thuc tinh thue nhap khau
    def tinh_thue_nhap_khau(self):
        return self.__gia * 0.1
    # phuong thuc get_ten
    def get_ten(self):
        return self.__ten
    # phuong thuc set_ten
    def set_ten(self):
        self.__ten = ten
    # phuong thuc get_gia
    def get_gia(self):
        return self.__gia
    # phuong thuc set_gia
    def set_gia(self):
        self.__gia = gia
    # phuong thuc get_giam_gia
    def get_giam_gia(self):
        return self.__giam_gia
    # phuong thuc set_giam_gia
    def set_giam_gia(self):
        self.__giam_gia = giam_gia