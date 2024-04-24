# Program to find if an entered number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            print(f"{i} times {num // i} is {num}")   # Can remove this line is want
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_4B.py
# Enter a number: 5
# 5 is a prime number
# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_4B.py
# Enter a number: 6
# 6 is not a prime number
# 2 times 3 is 6