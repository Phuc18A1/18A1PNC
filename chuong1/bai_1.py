class chunhat:
    def __init__(self,dai=0,rong=0):
        self.dai=dai
        self.rong=rong
    def nhap(self):
        self.dai=float(input('nhap chieu dai chu nhat: '))
        self.rong=float(input('nhap chieu rong chu nhat:'))

    def chuvi(self):
        return (self.dai + self.rong)*2
    def dientich(self):
        return(self.dai * self.rong)
    def xuat(self):
        print('\n---thong tin hinh chu nhat---')
        print(f'chieudai:{self.dai}')
        print(f'chieu rong: {self.rong}')
        print(f'chu vi: {self.chuvi()}')
        print(f'dien tich: {self.dientich()}')

if __name__=="__main__":
    cn=chunhat()
    cn.nhap()
    cn.xuat()