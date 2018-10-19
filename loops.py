my_list = [10, "test", 100, {12,34,40}]
for i in my_list:
    print(i)

my_set = {12,34,50,60,80,80,"hello"}

for i in my_set:
    print(i)

names = ["Mike","Matt","Nancy","Adam","Jenny","Nancy","Carl"];
empty_set=set()
#empty_set = names;
print(empty_set)
for i in names:
    empty_set.add(i)
print("Unique Names are",empty_set)
names= empty_set
print (names)
print (type(names))
# print (names[0])

user_wants = True;
while user_wants == True:
    print (10)
    user_wants = input("Please input if you want continue Y/N")=='Y'

known_people = ["Harish","Nagesh","Sumeet","Anusha"]
person = input("Enter the person you know : ")
if person in known_people:
    print ("You know this Person")
else:
    print ("You do not know this person")
print ("Formatinng {} and this Works".format(person))
