# Program to find alphabet, vowels, consonents, numbers, special characters
string = input("Enter a string : ")
s = string.replace(" ", "")
len = len(s)

alpha = vow = conso = num = spchar = 0
for i in range(0, len):
    x = s[i]
    if x.isalpha():
        alpha += 1
        if x.lower() in ('a', 'e', 'i', 'o', 'u'):
            vow +=1
        else:
            conso += 1
    elif x.isnumeric():
        num += 1
    else :
        spchar += 1

print("Number of alphabets : ", alpha)
print("Number of vowels : ", vow)
print("Number of consonants : ", conso)
print("Number of numbers : ", num)
print("Number of special characters : ", spchar)

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_2.py
# Enter a string :  13 hello !h
# Number of alphabets :  6
# Number of vowels :  2
# Number of consonants :  4
# Number of numbers :  2
# Number of special characters :  1