'''ar = [2,34,2,52,3,4]
sr = "ewrjfjwfo"

# print (length()
print ()


stre = "Tu hi Khuda"

print (stre.split())
# print(stre.replace(" " , "+"))
import time

current_date = time.strftime("%B %d, %Y")
print(current_date)

def remind(key,query):
    reminds = {None:None}
    reminds.update({key:query})
    if key == "None" or query == "None":
        pass
    return reminds

print(remind("Hello",'first reminder'))


file = open("reminder.txt" , "a") # used a for appending the data in the file 

file.write("Hellow world 2 ")

file.close()

file = open("reminder.txt" , 'a')

file.write("Hello world 3 ex.")

file.close()

dr = {1:"Hello"}    
dr.update({2:"Worldd"})

for i in dr:
    print(i , "-" , dr.get(i)'''
    
    
    
import pyperclip
reminder = "e"
reminder = pyperclip.paste()
print(pyperclip.paste())