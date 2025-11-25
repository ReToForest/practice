class Students :
    def __init__ (self , name , age , grades):
        self.name = name
        self.age = age
        self.grades = grades

    def ave_grade (self):
        grade = 0
        cnt = 0
        for i in self.grades :
            grade += i
            cnt += 1
        grade /= cnt 
        print("ave_grade = %.2f" %grade)
        
stu1 = Students("L",17,(100,99,99,100))
stu2 = Students("light",17,(99,100,98,99))

stu1.ave_grade()
stu2.ave_grade()
