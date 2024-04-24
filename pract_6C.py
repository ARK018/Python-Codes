# polymorphism is the ability of an object to take on many forms.
# Polymorphism allows us to define a class with a method that has the same name, but different implementations.
# The following example demonstrates polymorphism by defining two classes, Operation and Addition.
# The Operation class has a perform() method that is implemented in the Addition class.
# The perform() method is polymorphic because it can take on different implementations depending on the class that inherits from it.
# It is important to note that polymorphism is not limited to classes.
# It can also be used with functions and methods.
# Example
# Create a class called Operation
# Create a class called Addition that inherits from Operation
# Then create a function that demonstrates polymorphism
# Create an instance of Addition
# Create an instance of Subtraction
# Use the function with different operation objects

class Operation:
    def perform(self, num1, num2):
        pass  # Default operation

class Addition(Operation):
    def perform(self, num1, num2):
        result = num1 + num2
        print(f"Result of Addition: {result}")
        return result

class Subtraction(Operation):
    def perform(self, num1, num2):
        result = num1 - num2
        print(f"Result of Subtraction: {result}")
        return result

# Function that demonstrates polymorphism
def perform_operation(operation, num1, num2):
    return operation.perform(num1, num2)

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Create instances of Addition and Subtraction
addition = Addition()
subtraction = Subtraction()

# Using the function with different operation objects
perform_operation(addition, num1, num2)
perform_operation(subtraction, num1, num2)
