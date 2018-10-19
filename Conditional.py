a= int(input("Please input the Value"))
if a<5:
    print ("Less Than 5")
elif a==5:
    print ("Equal to 5")
else:
    print ("Greater than 5")

#Loop
mail =  ["m2@gmail.com","your*mail.com","test@testmail.com"]
names = ["Nagesh","Prathima","Guest"]
for i in mail:
    print(i)
#two Variables
for i,j in zip(names,mail):
    print(i,"\n This is ->",j)
