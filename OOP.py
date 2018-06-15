
#recursion
#python object oriented programming
    #encarpsulation
    #abstraction
    #inheritance
    #polymorphism

#classes and instances
#example1
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Audrey'
emp_1.last = 'Leonida'
emp_1.email = 'Audrey.Leonida@company.com'
emp_1.pay = '100000'

emp_2.first = 'Haisse'
emp_2.last = 'Bachuda'
emp_2.email = 'Haisse.Bachuda@company.com'
emp_2.pay = '10000'

print(emp_1.email)
print(emp_2.email)

#example2
class Employee:
    def __init__(self, first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'

    def fullname(self):
      return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Audrey', 'Leonida', '100000')
emp_2 = Employee('Haisse', 'Bachuda', '10000')

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

# print('{} {}'.format(emp_1.first,emp_1.last))
# print('{} {}'.format(emp_1.first,emp_2.first))

print(emp_1.fullname())
print(emp_2.fullname())







