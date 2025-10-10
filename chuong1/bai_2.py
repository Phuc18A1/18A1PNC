class sinhvien:
    def __int__(self,hoten,toan,ly,hoa):
        self.hoten=hoten
        self.toan=toan
        self.ly=ly
        self.hoa=hoa
    def nhap(self):
        self.hoten=input('nhap ho va ten thi sinh: ')
        self.toan=float(input('nhap diem toan cua sinh vien: '))
        self.ly=float(input('nhap diem ly cua sinh vien: '))
        self.hoa=float(input('nhap diem hoa cua thi sinh: '))
    def tong(self):
        return(self.toan + self.ly + self.hoa)
    def xuat(self):
        print(f"{self.hoten:20} | Toán: {self.toan:4.1f} | Lý: {self.ly:4.1f} | Hóa: {self.hoa:4.1f} | Tổng: {self.tong():5.1f}")


if __name__=='__main__':
    ds=[]
    n=int(input('nhap so luong thi sinh: '))
    print('\n===nhap danh sach thi sinh===')
    for i in range(n):
        print(f'\nthi dinh {i+1}:')
        ts=sinhvien()
        ts.nhap()
        ds.append(ts)
diemchuan=float(input('\nnhap diem chuan: '))
ds.sort(key=lambda x: x.tong(), reverse=True)
print("\n=== DANH SÁCH THÍ SINH ===")
for ts in ds:
    ts.xuat()

print(f"\n=== DANH SÁCH TRÚNG TUYỂN (điểm chuẩn {diemchuan}) ===")
for ts in ds:
    if ts.tong() >= diemchuan:
            ts.xuat()