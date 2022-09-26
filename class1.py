class Employee:
      def getdata(self):
            self.name="Ram"
            self.age = 34
            self.salary=45000
      def display(self):
            print("name : ",self.name)
            print("Age  : ",self.age)
            print("Salary : ",self.salary)

emp=Employee()
emp.getdata()
emp.display()
emp1=Employee()
emp1.getdata()
emp1.display()
