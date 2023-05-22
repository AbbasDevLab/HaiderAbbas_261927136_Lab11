from math import pi, sqrt

print("q.1")
class Shape:
    def __init__(self, sides):
        self.sides = sides
        
    def compute_area(self):
        pass

class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)
    
    def compute_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0) 
        self.radius = radius
    
    def compute_area(self):
        area = pi * self.radius ** 2
        return area

triangle_sides = [3, 4, 5]
triangle = Triangle(triangle_sides)
triangle_area = triangle.compute_area()
print("Area of triangle:", triangle_area)

circle_radius = 5
circle = Circle(circle_radius)
circle_area = circle.compute_area()
print("Area of circle:", circle_area)

print("q.2")
class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.EmpName = emp_name
        self.EmpID = emp_id
        self.Salary = salary
    
    def SalaryStatus(self):
        print("Employee Name:", self.EmpName)
        print("Employee ID:", self.EmpID)
        print("Salary:", self.Salary)

class BuildingManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 10000)

class ProcurementManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 12000)

class LogisticsManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 15000)

def main():
    employees = []
    
  
    building_manager = BuildingManager("Omer Sajid", "001")
    procurement_manager = ProcurementManager("Rehman Zafar", "002")
    logistics_manager = LogisticsManager("Ahmad", "003")
    
    
    employees.append(building_manager)
    employees.append(procurement_manager)
    employees.append(logistics_manager)
    
    
    for employee in employees:
        employee.SalaryStatus()
        print()
main()
