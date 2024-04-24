#Program for Exception Handling
try:
    print("a/b = ?")
    a = int(input("Enter Value of a: "))
    b = int(input("Enter Value of b: "))
    c = a / b
    print(c)

    n = int(input("Enter no. of elements to enter to the list: "))
    list1 = []
    for i in range(0, n):
        a = input("Enter element: ")
        list1.append(a)

    index = int(input("Enter index of the element to access from list(0 to %d): " % n))
    print("Element of the list you requested: ", list1[index - 1])

except IndexError:
    print("\nIndex Entered is not a valid index")
except ValueError:
    print("\nNumbers Only Allowed")
except ZeroDivisionError:
    print("\nDivide By Zero Not Allowed\n")


# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_6A.py
# a/b = ?
# Enter Value of a: 4
# Enter Value of b: 0

# Divide By Zero Not Allowed

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_6A.py
# a/b = ?
# Enter Value of a: 4
# Enter Value of b: 2
# 2.0
# Enter no. of elements to enter to the list: 3
# Enter element: 1
# Enter element: 2
# Enter element: 3
# Enter index of the element to access from list(0 to 3): 5

# Index Entered is not a valid index