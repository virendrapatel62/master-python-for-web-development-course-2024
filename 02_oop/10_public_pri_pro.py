class A:
    def __init__(self) -> None:
        self.__name_a = "A Class member"
        # you will not access outside of the class, only access in subsclass
        self._name = "Protected member"

    def getName(self):
        return self.__name_a


class B:
    def __init__(self) -> None:
        self.name_b = "B Class member"


class C(A, B):
    def __init__(self) -> None:
        A.__init__(self)
        B.__init__(self)
        self.name_c = "C classs Member"


c = C()

print(c.name_c)
print(c.name_b)

a = A()
print(a.getName())
print(a._name)
