def add_number(list):
    return sum(list)

print(add_number([2,3,4,5,6,7,8,9]))

#using Args and kwargs
def add_using_args(num1,num2,*args, **kwargs):
    print (args)
    print(kwargs)
    return sum(args + (num1,num2))

print(add_using_args(2,3,4,5,6,7,8,9,test=100,test2=200))

def methodcall(another):
    return another();

def add_two_number():
    return 35 + 77;

print(methodcall(add_two_number))

print(methodcall(lambda: 35 +77))
#Little More of lambda

val = (lambda x: x*3)(5)
#Above one is exactly same as
# def f(x):
#     retrun x *3;
# f(5)
print(val)


#List Comprehension
my_list = [x * 3 for x in range(10)]
print(my_list)

#Even Numbers my_list
even_list = [n for n in range(21) if n % 2 == 0]
print(even_list)

#------------------------


my_list = [13,15,18,20,28,45,56];
my_even_list = list(filter(lambda x: x%2 == 0,my_list))
#my_even_list = list(lambda x: x%2 == 0,my_list)
print ("This is my_even_list", my_even_list)

def even (x):
    return x%2 == 0;

#Instead of Lambda we can also use a function for filter
new_list = [13,15,18,20,28,45,56];
my_new_even_list = list(filter(even,new_list))
print(my_new_even_list)
