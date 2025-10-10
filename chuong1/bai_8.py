class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    def display(self):
        print(f"Tên nhân viên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào làm: ", end="")
        self.start_date.display()

birth = Date(5, 4, 1999)
start = Date(1, 6, 2022)
emp = Employee("Nguyễn Văn A", birth, start)
emp.display()

