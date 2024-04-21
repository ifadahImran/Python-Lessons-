#String
x = "python{}"
y = 'elephant'
#docstring
z = """\n Hello World
can include paragraphs 
"""

#Print 
#print(x,y,z)

#to findout the data type
#print(type (x))

#to findout the data type with the output 
#print(type (x),x)

#print only the 0th index (first character)
#print(x[0])

#print only the one before last index 
#print(x[-2])

#INT
a=0

#to findout the data type
#print(type (a))

#concat
#print(x,a)
#print(x.format(a))
#print(x+y+str(a))
#print(f"Ifadah {y}")

#FLOAT
b =0.0 
#print(type(b))

#print("Github Configer")

#List 
l1 =[1,2,3,"ifadah", 0.0]
#print(l1)
#print(l1[0:4])
#print(len(l1))

#TUPLE
tuple1 =(1,2,3,4)
#print(tuple1)

#BOOLEAN
is_created = False
is_failed = True
#print(is_created, type(is_created))

if 2>0:
    is_created=True

    #print(is_created)

#SET
set1= set([1, 2, "Geeks", "Geeks", 3, 2])
#print(set1)

#DICTIONARY
dict = {}
dict1 = {
    "Name": "Ifadah",
    "age": 19, 
    "mobile": '0777494050'
}

print(dict1['Name'])

dict2= {
    "Name": "Inaam",
    "age": 19, 
    "mobile": '0777935930'
}

#Create list of dictionaries
print(dict1['mobile'])
list =[]
list.append(dict1)
list.append(dict2)
print(list)

import pandas as pd 

df = pd.DataFrame(list)
print(df.head())
print(type(df))