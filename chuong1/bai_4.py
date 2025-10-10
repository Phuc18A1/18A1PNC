class Stack:
    def __init__(self, size):
        self.size = size
        self.data = []

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.size

    def push(self, value):
        if not self.isFull():
            self.data.append(value)
        else:
            print(" Ngăn xếp đã đầy!")

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            print(" Ngăn xếp rỗng!")
            return None

st = Stack(3)
st.push(10)
st.push(20)
st.push(30)
st.push(40)     
print(st.pop()) 
print(st.pop()) 
print(st.pop()) 
print(st.pop()) 