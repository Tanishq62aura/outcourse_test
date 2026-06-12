####QUE!

class employee:
    __salary = 50000

    def increment(self):
        self.__salary += 100000
    def deduct(self):
        self.__salary -= 5000

    def getsalary(self):
        print(self.__salary)

e1 = employee()
e2 = employee()

print("employee1")
e1.getsalary()
e1.increment()
e1.getsalary()
e1.deduct()
e1.getsalary()

print("employee2")
e2.getsalary()
e2.increment()
e2.getsalary()
e2.deduct()
e2.getsalary()
