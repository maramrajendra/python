#Employee class

class Employee:

    __ecount = 0

    #constructor - It doesn't return values

    def __init__(self, eid, ename, esal, design):
        self.EmpId = eid
        self.EName = ename
        self.Salary = esal
        self.Designation = design
        Employee.__ecount+=1

    def Display(self):
        print("\nId=", self.EmpId)
        print("\n Name=", self.EName)

    @staticmethod
    def ShowEmployeeCount():
        print("No of Employees", Employee.__ecount)
    

    #destructor
    def __del__(self):
        print("Destructor called")

def main():
    e1 = Employee(1, 'Raj', 88, 'SE')
    e2 = Employee(1, 'Raj1', 88, 'SE')

    Employee.ShowEmployeeCount()
    e1.Display()

main()


