class Demo:
    a = 4
    b = 6

    @classmethod
    def sum(cls):
        print(f"{cls.a} + {cls.b} = {cls.a + cls.b}")

class Demo01(Demo):
    a = 5


obj = Demo()
obj1 = Demo01()
print(obj1.a)
obj1.sum()
# without using class method decoreter value a is overwrite so
obj1.sum()

