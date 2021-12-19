
class Calculator:


    def __init__(self):
        self.result=0

    def add(self,num):
        self.result += num
        return self.result


cal1 = Calculator()


print(cal1.add(3))
print(cal1.add(5))






import Sub_func


test = 0
sm=Sub_func(test)

sm.print_test()
