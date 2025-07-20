class Calculator():
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return 0
        return a / b

if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(1,3))
    print(cal.substract(3, 1))
    print(cal.divide(1, 3))
    print(cal.divide(1, 0))
