
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']

test = zip(list1, list2)  # zip the values

testList = list(test)

a, b = zip( *testList )
print('The first list was ', list(a));
print('The second list was ', list(b));



a = 10
while a > 0:
    print(a)
    break
else:
    print('Now the value of a is ',a);
