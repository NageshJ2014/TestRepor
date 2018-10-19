class Student:
    def __init__(self,name,school,marks=[]):
        self.name=name;
        self.school=school
        self.marks=marks
    def average(self):
        return sum(self.marks)/len(self.marks);

    @classmethod
    def classmethod_print(cls1):
        print ("This is the Class Method")

    @staticmethod
    def staticmethod_print(name="test"):
        print("It Prints the Static Method {}".format(name))



Nagesh = Student("Nagesh","DSCE",[90,95,97,99,100])
#print(Nagesh)
print(Nagesh.marks)
Student.classmethod_print();
Nagesh.classmethod_print()
Nagesh.staticmethod_print(Nagesh.name + "Hello")


#Student_list = [Student(x,y) for x in ["Nagesh","Harish","Anusha N", "Sumeet Kumer"] for y in range(len(x)) ]
#print(Student_list)

#print (x,y for x in ["Nagesh","Harish","Anusha N", "Sumeet Kumer"] for y in range(len(x)))


class store:
    def __init__(self,name="My Store"):
        self.name = name;
        self.items = [];

    def add_items(self,name,price):
        item = {"name":name,"price":price};
        self.items.append(item);
    def stock_prize(self):
        return sum(item['price'] for item in self.items)

NJ = store("Nagesh Store");
NJ.add_items("Raagi",700);
NJ.add_items("Rice",500);
NJ.add_items("Toor Dal",1200)

print(NJ.stock_prize())
