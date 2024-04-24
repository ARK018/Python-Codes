# #Employee Class Program
# class Employee:

#     def getData(self, empid, name, dept, salary, specialized):
#         self.name = name
#         self.salary = salary
#         self.empid = empid
#         self.dept = dept
#         self.specialized = specialized

#     def displayEmployee(self):
#         print("\nEmployee Details--")
#         print("Employee ID :", self.empid, "\nEmployee Name:", self.name,
#               "\nDepartment:", self.dept, "\nEmployee Salary:", self.salary,
#               "\nEmployee Specialization:", self.specialized)

# empid = int(input("Enter Employee ID: "))
# name = input("Enter Employee Name: ")
# dept = input("Enter Department of Employee: ")
# salary = int(input("Enter Salary of Employee: $"))
# specialized = input("Enter Field of Specialization: ")

# emp1 = Employee()
# emp1.getData(empid, name, dept, salary, specialized)
# emp1.displayEmployee()

# # PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_5A.py
# # Enter Employee ID: 1
# # Enter Employee Name: Ak
# # Enter Department of Employee: IT
# # Enter Salary of Employee: $1000000
# # Enter Field of Specialization: A.I.                    

# # Employee Details--
# # Employee ID : 1
# # Employee Name: Ak
# # Department: IT
# # Employee Salary: 1000000
# # Employee Specialization: A.I.




#FOR MULTIPLE USERS
# class Employee:
#     empCount = 0
#     employees = []  # List to store employee instances

#     def getData(self, empid, name, dept, salary, specialized):
#         self.name = name
#         self.salary = salary
#         self.empid = empid
#         self.dept = dept
#         self.specialized = specialized
#         Employee.empCount += 1
#         Employee.employees.append(self)  # Add current employee instance to the list

#     @classmethod
#     def displayCount(cls):
#         print(f"Total Employee {cls.empCount}")

#     @classmethod
#     def displayAllEmployees(cls):
#         print("\nAll Employees Details--")
#         for emp in cls.employees:
#             emp.displayEmployee()

#     def displayEmployee(self):
#         print("\nEmployee Details--")
#         print("Employee ID :", self.empid, "\nEmployee Name:", self.name,
#               "\nDepartment:", self.dept, "\nEmployee Salary:", self.salary,
#               "\nEmployee Specialization:", self.specialized)

# # Prompt user to enter employee details
# emp_count = int(input("Enter the number of employees: "))
# for i in range(emp_count):
#     empid = int(input("Enter Employee ID: "))
#     name = input("Enter Employee Name: ")
#     dept = input("Enter Department of Employee: ")
#     salary = int(input("Enter Salary of Employee: $"))
#     specialized = input("Enter Field of Specialization: ")

#     # Create Employee instance and store employee details
#     emp = Employee()
#     emp.getData(empid, name, dept, salary, specialized)

# # Display total employee count and details of all employees
# Employee.displayCount()
# Employee.displayAllEmployees()

# PS C:\Users\kambl\Desktop\Programs\ARK_PY\practice> python pract_5A.py
# Enter the number of employees: 2
# Enter Employee ID: 1
# Enter Employee Name: A
# Enter Department of Employee: A
# Enter Salary of Employee: $1
# Enter Field of Specialization: A
# Enter Employee ID: 2
# Enter Employee Name: B
# Enter Department of Employee: B
# Enter Salary of Employee: $1
# Enter Field of Specialization: B
# Total Employee 2

# All Employees Details--

# Employee Details--
# Employee ID : 1
# Employee Name: A
# Department: A
# Employee Salary: 1
# Employee Specialization: A

# Employee Details--
# Employee ID : 2
# Employee Name: B
# Department: B
# Employee Salary: 1
# Employee Specialization: B
