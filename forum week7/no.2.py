import os
os.chdir('c:/Users/Asus/Desktop')
file = open("test.txt","r")
new = open("newtest.txt","w")
count = 0

for line in file:
    count += 1
    new.write("{:2d} {}".format(count,line))
new.close()