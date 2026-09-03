class Student:
    count=0
    total_gpa=0

    def __init__ (self,name,gpa):
        self.name= name
        self.gpa= gpa
        Student.count +=1
        Student.total_gpa += gpa

    def get_info(self):
       return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"total no. of students : {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
         return 0
        return cls.total_gpa / cls.count

student1= Student("nishi",8.9)
student2= Student("mishi",8.7)

print(Student.get_count())
print(Student.get_average_gpa())
