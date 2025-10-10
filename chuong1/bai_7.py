class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    def next_day(self):
        self.day += 1
        if self.day > 30:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1



d = Date(30, 12, 2024)
d.display()      
d.next_day()
d.display()      