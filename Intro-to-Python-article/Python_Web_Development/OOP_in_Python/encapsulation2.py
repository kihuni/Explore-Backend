class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id   # Private attribute
        self.__name = name    # Private attribute      
        self.__salary = salary # Private attribute 

    # Getter method to access the private attribute
    def get_emp_id(self):
        return self.__emp_id
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    # Setter method to modify the salary attribute
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            
        else:
            print("invalid salary value. Salary must be > 0")
            
# Creating an instance of Employee
employe1 = Employee(101, "John Doe", 5000)
employe2 = Employee(102, "Jane Doe", 6000)

# Accessing methods (encapsulation hides the implementation details)
print("Employee ID:", employe1.get_emp_id())
print("Name:", employe1.get_name())


# Modifying the salary attribute using setter method
employe1.set_salary(7000)
print("Salary:", employe1.get_salary())