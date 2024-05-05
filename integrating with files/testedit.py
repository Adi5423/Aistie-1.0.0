import os
path = 'D:\Py_Start\Programming\Projects\Laptop Assistant\integrating with files\\reminders.txt'


def reader(reminds, key):
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines:
            index = line.find("-")
            if line[:index].strip() == key:
                output = line
                return output












'''file = open(path , "a") # used a for appending the data in the file 
print("Hellow world 2" , file = file , end ='\n')
# file.write("Hellow world 2 ")

file.close()

file = open(path , 'a')
print("Hello world 3 ex." , file = file , end ='\n')

# file.write("Hello world 3 ex.")

file.close()'''