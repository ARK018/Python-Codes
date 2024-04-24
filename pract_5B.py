class Employee:

    def __init__(self, empid, name, dept, salary, specialized):
        self.name = name
        self.salary = salary
        self.empid = empid
        self.dept = dept
        self.specialized = specialized

    def displayEmployee(self):
        print("\n\nEmployee Details--")
        print("Employee ID : ", self.empid, "\nEmployee Name: ", self.name,
              "\nDepartment: ", self.dept, "\nEmployee Salary: ", self.salary,
              "\nEmployee Specialization: ", self.specialized)


# Get input from the user
empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
dept = input("Enter Department of Employee: ")
salary = int(input("Enter Salary of Employee: "))
specialized = input("Enter Field of Specialization: ")

# Create an instance of the Employee class
emp1 = Employee(empid, name, dept, salary, specialized)

# Display the employee details
emp1.displayEmployee()


# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_5B.py
# Enter Employee ID: 1
# Enter Employee Name: Ak
# Enter Department of Employee: IT
# Enter Salary of Employee: 1000000
# Enter Field of Specialization: A.I.


# Employee Details--
# Employee ID :  1
# Employee Name:  Ak
# Department:  IT
# Employee Salary:  1000000
# Employee Specialization:  A.I.