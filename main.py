
class Student:

    def __init__(self, name, nim):
        self.name = name
        self.nim = nim
    
    def getName(self):
        return self.name

    def getNIM(self):
        return self.nim
    
    def name(a):
        return a
    def NIM(a):
        return a



def main():
    name1 = Student.name("Briant")
    name2 = Student.name("Alexander")
    NIM1 = Student.NIM(2802453471)
    NIM2 = Student.NIM(2802460962)
    print(name1, NIM1)
    print(name2, NIM2)    


if __name__ == "__main__":
    main()
