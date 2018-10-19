class Student:
    def __init__(self,name,school,marks=[]):
        self.name=name;
        self.school=school
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks);
    @classmethod
    def friend(cls,origin,friend_name):
        print ("It Came to Student Class Method")
        return cls(friend_name,origin.school)

NJ = Student("Nagesh","DSCE",[20,30,40]);
friend = NJ.friend(NJ,"Harsha");
print (friend.name,friend.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,marks,salary):
        super().__init__(name,school,marks)
        self.salary = salary;

    @classmethod
    def friend(cls,origin,friend_name,salary):
        print ("It Came to WorkingStudent Class Method")
        return cls(friend_name,origin.school,origin.marks,salary)

Prathima = WorkingStudent("Prathima Nagesh","SJCIT",[80,80,90,92],23.40)
print(Prathima.salary)
friend = Prathima.friend(Prathima,"Harsha",400);
print(friend.salary)
