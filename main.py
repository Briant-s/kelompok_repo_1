
def askUser(query):
    return input(f'Input {query}: ')



class Student:

    def __init__(self, name = "", gender = "", age = 0, nim = 0):
        self.name = name
        self.gender = gender
        self.age = age
        self.nim = nim
        
    def askDetails(self):
        self.name = askUser('Name')
        self.gender = askUser('Gender')
        self.age = askUser('Age')
        self.nim = askUser('Nim')
        

    def getDetails(self):
        print(f'''
            Name: {self.name}
            Gender: {self.gender}
            Age : {self.age}
            NIM : {self.nim}''')




def main():
    student_1 = Student()
    print('Enter Details for Student 1')
    student_1.askDetails()

    student_2 = Student()
    print('Enter Details for Student 2')
    student_2.askDetails()

    print('Student 1 Details : ')
    student_1.getDetails()
    print('Student 2 Details : ')
    student_2.getDetails()


    #student_1 = Student("Briant", "2802453471")
    #student_2 = Student("Alexander", "2802460962")


if __name__ == "__main__":
    main()
