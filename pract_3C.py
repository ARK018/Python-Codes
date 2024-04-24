# Program to perform dictionary operations in python

student1 = {'ID':1, 'Name':'Akshay', 'Dept':'IT'}
student2 = {'ID':2, 'Name':'Chetan', 'Dept': 'IT'}

print("Dictionaries")
print(student1)
print(student2)

#Get Student data from user
student3 = {}
print("Enter student3 details")
student3['ID'] = input("Enter student id : ")
student3['Name'] = input("Enter student name : ")
student3['Dept'] = input("Enter student department : ")

print("\nStudent3 details")
print(f"ID : {student3['ID']}")
print(f"Name : {student3['Name']}")
print(f"Department : {student3['Dept']}")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_3C.py
# Dictionaries
# {'ID': 1, 'Name': 'Akshay', 'Dept': 'IT'}
# {'ID': 2, 'Name': 'Chetan', 'Dept': 'IT'}
# Enter student id : 3
# Enter student name : Raj
# Enter student department : Computer

# Student 3 details
# ID : 3
# Name : Raj
# Department : Computer