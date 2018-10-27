class TestA():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        self.hobby = "Swimming"

class TestB():
    def __init__(self, parent):
        self.name = parent.name
        self.age = parent.age

        self.hobby = parent.hobby

objA = TestA("Jon", "18")
objB = TestB(objA)

print(objA.hobby)
print(objB.hobby)
