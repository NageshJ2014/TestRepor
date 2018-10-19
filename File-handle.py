done_det=open("test.txt","r")
contents = done_det.readlines()
file_write = open("check.txt","w")
for i in contents:
    #print(i)
    file_write.write(i)
#print (contents)
done_det.close();
file_write.close();
print ("\n_\t_\t_\t_\n|\t|\t|\t|")
print ("_\t_\t_\t_\n|\t|\t|\t|")
print ("_\t_\t_\t_\n|\t|\t|\t|")
with open("check.txt","a+") as file:
    file.seek(0);
    contents = file.readlines()
    print (contents);
    file.write("\nAdding the last line")
