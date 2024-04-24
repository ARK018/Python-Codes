# Program to implement inheritance in python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This will be implemented by the child classes

# Child class 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child class 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Get input for Dog
dog_name = input("Enter the name of the dog: ")
dog = Dog(dog_name)

# Get input for Cat
cat_name = input("Enter the name of the cat: ")
cat = Cat(cat_name)

# Calling the speak method of each instance
print(dog.speak())  # Output: Dog's sound based on the input name
print(cat.speak())  # Output: Cat's sound based on the input name

#***********OUTPUT**********
# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_6B.py
# Enter the name of the dog: Buddy
# Enter the name of the cat: Whiskers
# Buddy says Woof!
# Whiskers says Meow!
