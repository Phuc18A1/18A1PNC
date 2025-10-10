class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []
        self.count = 0

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.size

    def push(self, value):
        if not self.isFull():
            self.data.append(value)
            self.count += 1
        else:
            print(" Ngăn xếp đầy!")

    def pop(self):
        if not self.isEmpty():
            self.count -= 1
            return self.data.pop()
        else:
            print(" Ngăn xếp rỗng!")
            return None
st = Stack(2)
st.push(5)
st.push(8)
print("Số phần tử:", st.count)
st.pop()
print("Số phần tử:", st.count)