class ChuNhat:
    def __init__(self, rong, dai):
        self.rong = rong
        self.dai = dai
    def chuvi(self):
        return (self.dai + self.rong) * 2
    def dientich(self):
        return self.dai * self.rong
    def xuat(self):
        print(f'Chieu dai: {self.dai}')
        print(f'Chieu rong: {self.rong}')
        print(f'Chu vi: {self.chuvi()}')
        print(f'Dien tich: {self.dientich()}')
class Vuong(ChuNhat):
    def __init__(self, rong, dai):
        super().__init__(rong, dai)