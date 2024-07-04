class A:
    def method(self):
        print("I am class A")

class B:
    def method(self):
        print("I am class B")
        super().method()
class C(A,B):
    def method(self):
        print("I am class C")
        super().method()

obj = C()
obj.method()