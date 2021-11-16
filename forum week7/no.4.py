import re
import os
os.chdir('c:/Users/Asus/Desktop')

def splitting_sentence(new):
    file = open(new,"r")
    read = file.read()
    result = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', read)
    for i in result:
        print(i)
    file.close()

splitting_sentence("sentence.txt")