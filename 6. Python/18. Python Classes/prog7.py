#class Method

class Student:
    school = "Manac Infotech"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("Manac School")
print(Student.school)