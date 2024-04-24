# # Program to perform list operations in python

# FOR STRING VALUES
list1 = ['0', '1', '2', '3', '4']
list2 = ['5', '6', '7', '8', '9']

print(list1)
print(list2)

list1.extend(list2)
print(f"Extended list (List1 + list2) = {list1}")

new_element = (input("Enter a new element to add to the list : "))
list1.append(new_element)
print(f"Adding {new_element} to list : {list1}")

list1.reverse()
print(f"Reversed list : {list1}")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_3A.py
# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_3A.py
# ['0', '1', '2', '3', '4']
# ['5', '6', '7', '8', '9']
# Extended list (List1 + list2) = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Enter a new element to add to the list : 10
# Adding 10 to list : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Reversed list : ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']



# FOR INTEGER VALUES
# list1 = [0, 1, 2, 3, 4]
# list2 = [5, 6, 7, 8, 9]

# print(list1)
# print(list2)

# list1.extend(list2)
# print(f"Extended list (List1 + list2) = {list1}")

# new_element = int((input("Enter a new element to add to the list : ")))
# list1.append(new_element)
# print(f"Adding {new_element} to list : {list1}")

# list1.reverse()
# print(f"Reversed list : {list1}")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_3A.py
# [0, 1, 2, 3, 4]
# [5, 6, 7, 8, 9]
# Extended list (List1 + list2) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Enter a new element to add to the list : 10
# Adding 10 to list : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Reversed list : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
