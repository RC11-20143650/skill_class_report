def plus(a, b):
    answer = a + b
    return answer

A = 1
B = 2

calculation = plus(A, B)
print(calculation)

test_02 = 'a'
print(test_02)

class Car:
    def __init__(self, window, wheel):
        self.window = window
        self.wheel = wheel
    def myfunc(self):
        print("This car has "+str(self.window)+
        " windows and "+str(self.wheel)+" wheels")
test = Car(3, 2)
test.myfunc()
