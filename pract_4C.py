# Program to check if the entered number is prime or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_4C.py
# Enter a number: 153
# 153 is an Armstrong number.
# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_4C.py
# Enter a number: 32
# 32 is not an Armstrong number.