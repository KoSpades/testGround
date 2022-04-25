class Person:

    def __init__(self, age):
        self.age = age

    def return_old_me(self):
        print(self.age*10)


if __name__ == "__main__":
    steven = Person(10)
    steven.return_old_me()
