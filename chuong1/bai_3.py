
class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau if mau != 0 else 1

    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        while self.mau == 0:
            print(" Mẫu số không được bằng 0. Nhập lại!")
            self.mau = int(input("Nhập mẫu số: "))

    def hop_le(self):
        # kiểm tra phân số có hợp lệ không (mẫu khác 0)
        return self.mau != 0

    def __str__(self):
        # trả về dạng hiển thị đẹp của phân số
        return f"{self.tu}/{self.mau}"

# --- Chương trình chạy thử ---
if __name__ == "__main__":
    ps = PhanSo()
    print("Nhập phân số:")
    ps.nhap()

    if ps.hop_le():
        print(" Phân số hợp lệ!")
        print("Phân số vừa nhập là:", ps)
    else:
        print(" Phân số không hợp lệ!")