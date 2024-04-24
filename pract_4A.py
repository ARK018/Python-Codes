# Program to print fibonacci series
def fibo(i):
    if i == 0:
        return i
    elif i == 1:
        return i
    else:
        return fibo(i - 1) + fibo(i - 2)
    
n = int(input("Enter no. of terms to print : "))
if n <= 0:
    print("Enter a positive integer.")
else:
    for i in range(0, n):
        print(f"Fibonacci term {i + 1} : {fibo(i)}")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_4A.py
# Enter no. of terms to print : 6
# Fibonacci term 1 : 0
# Fibonacci term 2 : 1
# Fibonacci term 3 : 1
# Fibonacci term 4 : 2
# Fibonacci term 5 : 3
# Fibonacci term 6 : 5