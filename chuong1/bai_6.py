class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []

    def push(self, value):
        if len(self.data) < self.size:
            self.data.append(value)
        else:
            print("Ngăn xếp đầy!")

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            print("Ngăn xếp rỗng!")

    def print(self):
        print("Nội dung ngăn xếp:", self.data)

st = Stack(3)
st.push(2)
st.push(4)
st.push(6)
st.print()