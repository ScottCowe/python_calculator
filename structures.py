class Stack:
    def __init__(self):
        self.stack_arr = []
        self.length = 0

    def push(self, value):
        self.stack_arr.append(value)
        self.length += 1

    def pop(self):
        try:
            value = self.stack_arr[-1]
            self.stack_arr = self.stack_arr[:-1]
            self.length -= 1
            return value
        except:
            print(f"Stack length is {self.length}")
            print(f"Stack is {self.asString()}")
            raise Exception("Could not pop stack")

    def peek(self):
        try:
            return self.stack_arr[-1]
        except:
            return ""

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def asString(self):
        result = "["

        for i in self.stack_arr:
            result += i + ", "

        return result + "]"
