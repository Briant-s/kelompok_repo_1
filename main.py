def askUser(query):
    return input(f'Input {query}: ')

class Student:

    def __init__(self, name = "", gender = "", age = 0, nim=""):
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

class Alumni(Student):
    def __init__(self, name="", gender="", age=0, nim="", gpa=0, degree=""):
        super().__init__(name, gender, age, nim)
        self.gpa = gpa
        self.degree = degree

    def askDetails(self):
        super().askDetails()
        self.gpa = askUser('GPA')
        self.degree = askUser('Degree')
    
    def getDetails(self):
        super().getDetails()
        print(f'''            GPA: {self.gpa}
            Degree: {self.degree}''')

def ask_user_details(person, i):
    print(f'Enter details for {type(person).__name__} {i}')
    person.askDetails()

def fetch_user_details(person):
    person.getDetails()

def main():

    total_students = int(input('Enter number of students: ')) 
    total_alumnis = int(input('Enter number of alumnis: '))
    
    students = [Student() for _ in range(total_students)]
    alumnis = [Alumni() for _ in range(total_alumnis)]

    for i, student in enumerate(students, start = 1):
        ask_user_details(student, i)

    for i, alumni in enumerate(alumnis, start = 1):
        ask_user_details(alumni, i)

    for i, student in enumerate(students, start = 1):
        print(f'Details for Student {i}: ')
        fetch_user_details(student)

    for i, alumni in enumerate(alumnis, start = 1):
        print(f'Details for Alumni {i}: ')
        fetch_user_details(alumni)


if __name__ == "__main__":
    main()
