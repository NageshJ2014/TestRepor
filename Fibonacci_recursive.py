def fibonaaci(pos):
    if pos == 1:
        #print('0')
        return 0
    if pos == 2:
        #print('1')
        return 1;
    n1 = fibonaaci(pos -1);
    n2 = fibonaaci (pos -2);
    print (n1)
    return n1 + n2;

n5 = fibonaaci ( 5);
print(n5);



name = 'Andy'  # define name


def printBob():
   global name;
   print('printing from the def: ', name)  # print from function
   name = 'Bob'  # define name in function
   print('printing from the def: ', name)  # print from function

# the main function
print('printing from the main:{}  Before Global Change '.format(name))  # print from the main
printBob()  # call the function to print
print('printing from the main: ', name)  # print from the main



num = input('Enter a number : ')
print('The zero-padded number is : ', str(num).rjust(10,'0'))
