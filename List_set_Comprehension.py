numbers = [ 1,2,3,4,5,6,7,8,9,10]

# def even_numbers():
#     evens = []
#     for i in numbers:
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
#
# print(even_numbers([12,24,25,26,18,19,44,47,50]))

def who_do_you_know():
    people = input("Please input the Names of the People Separated by Commas")
    people_list= (people.strip()).split(",")
    return people_list

def ask_user():
    person = input("Please input the Name of the Person You think You know")
    if person in who_do_you_know():
        print("You know Mr./Ms. {}".format(person))
    else:
        print("You Do not know Mr./Ms. {}".format(person))

#ask_user()

my_list = [x * 3 for x in range(10)]
print(my_list)

#Even Numbers my_list
even_list = [n for n in range(21) if n % 2 == 0]
print(even_list)

#With 'Strings'
people_we_know = "Rajesh,Nagesh,SUMEET,HarshA,ANUSHA Nagesh";
print(people_we_know)
people_we_know = [person.strip().capitalize() for person in people_we_know.split(",")]
print(people_we_know)

posts = [
    {
     'author':'Corey Anderson',
     'title': 'Blog Post 1',
     'Content': 'FIrst Post Content',
     'date':'April 20, 2018'
    },
    {
     'author':'Bill Gates',
     'title': 'Blog Post 2',
     'Content': 'Microsoft Product Announcements',
     'date':'April 29, 2018'
    }
]

print(posts)
my_dict = {
 'author':'Corey Anderson',
 'title': 'Blog Post 1',
 'Content': 'FIrst Post Content',
 'date':'April 20, 2018'
}
print ("\n")
print(my_dict)
for i in my_dict:
    print (my_dict[i])

new_dict = {x['author']:x['title'] for x in posts}
print(new_dict)
