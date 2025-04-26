class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        raise TypeError("Operand must be an instance of Employee")
    
    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.salary == other.salary
        raise TypeError("Operand must be an instance of Employee")
    
# Example usage:
if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    
    print("Combined Salary:", emp1 + emp2)
    print("Salary Difference:", emp1 - emp2)
    print("Is Alice's salary less than Bob's?", emp1 < emp2)
    print("Is Alice's salary greater than Bob's?", emp1 > emp2)
    print("Do they have the same salary?", emp1 == emp2)
