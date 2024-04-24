try:
    a = 0
    while a <= 3:
        print("\n1. Create And Write\n2. Append\n3. Read\n4. Exit")
        a = int(input("Enter Choice: "))
        if a == 1:
            file_name = input("Enter File Name To Create: ")
            f = open(file_name + ".txt","w+")
            text = input("Enter Text to add to the file: ")
            f.write(text)
        if a == 2:
            text2 = input("Enter Text To Append To The File: ")
            f = open(file_name+".txt","a")
            f.write(" " + text2)

        if a == 3:
            f = open(file_name+".txt","r")
            if f.mode == 'r':
                contents = f.read()
                print("Printing Contents Of File (%s.txt)\n\n" % file_name)
                print(contents)
        
        if a == 4:
            print("Exiting Program")
            break

except IOError:
    print("File Not Found")

finally:
    f.close()

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_7.py

# 1. Create And Write
# 2. Append
# 3. Read
# 4. Exit
# Enter Choice: 1
# Enter File Name To Create: hello
# Enter Text to add to the file: Hello

# 1. Create And Write
# 2. Append
# 3. Read
# 4. Exit
# Enter Choice: 2
# Enter Text To Append To The File: World

# 1. Create And Write
# 2. Append
# 3. Read
# 4. Exit
# Enter Choice: 3
# Printing Contents Of File (hello.txt)


# Hello World

# 1. Create And Write
# 2. Append
# 3. Read
# 4. Exit
# Enter Choice: 4
# Exiting Program
