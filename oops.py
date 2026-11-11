class Student:
    def __init__(self, name, branch):
        self.name = name          # attributes (data)
        self.branch = branch

    def introduce(self):          # method (behavior)
        print(f"Hi, I'm {self.name} from {self.branch}")

# Creating objects from the class
s1 = Student("Abhi", "ECE")
s2 = Student("Arun", "CSE")

s1.introduce()   # Hi, I'm Abhi from ECE
s2.introduce()   # Hi, I'm Arun from CSE