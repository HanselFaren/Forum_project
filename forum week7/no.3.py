import os
os.chdir('c:/Users/Asus/Desktop')
poem = open("66689-0.txt","r")
look = poem.read()
lower_case = look.lower()

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for ele in lower_case:
	if ele in punc:
		new_poem = lower_case.replace(ele, "")

text = new_poem.split()
count1 = 0
count2 = 0
for a in text:
	count3 = count1 + len(a)
	count4 = count2 + 1

average = count3/count4
print(average)
