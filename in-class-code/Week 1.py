# Week 1

# class CreditCard:
#     def __init__(self, customer, bank, account, balance, limit):
#         self._customer = customer
#         self._bank = bank
#         self._account = account
#         self._balance = balance
#         self._limit = limit
    
#     def get_customer(self):
#         return self._customer
    
#     def get_bank(self):
#         return self._bank
    
#     def get_balance(self):
#         return self._balance
    
#     def get_account(self):
#         return self._account

#     def get_limit(self):
#         return self._limit

#     def make_payment(self, amount):
#         if amount > self._balance:
#             print('Payment declined.')
#         else:
#             self._balance -= amount
#         return self._balance
    
#     def charge(self, amount):
#         if self._balance + amount > self._limit:
#             print('x')
#         else:
#             self._balance += amount
#         return self._balance


# n = CreditCard('Ngoc', 'VCB', 12345, 100_000, 10_000_000)
# print(n.make_payment(50_000))
# print(n.get_balance())
# print(n.make_payment(500_000))

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"({self.x}, {self.y})"
    
#     def __mul__(self, n):
#         return self.x*n, self.y*n

#     def __add__(self, other):
#         return self.x+other.x, self.y+other.y

#     def __sub__(self, other):
#         return self.x-other.x, self.y-other.y

#     def __pow__(self, other):
#         return self.x*other.x + self.y*other.y

# v1 = Vector(3,2)
# v2 = Vector(1,3)

# v3 = v1+v2
# print(v3)

# v4 = v1*2
# print(v4)

# v5 = v1**v2
# print(v5)

class Person:
    def __init__(self, name, id, age, gender):
        self._name = self.validate_name(name)
        self._id = self.validate_id(id)
        self._age = self.validate_age(age)
        self._gender = self.validate_gender(gender)

    def __repr__(self) -> str:
        return f"Name: {self._name}\nID: {self._id}\nAge: {self._age}\nGender: {self._gender}"

    def validate_name(self, name):
        if str(name).isalpha():
            return name
        else:
            print('Name only accepts input of string data type.')
    
    def validate_id(self, id):
        try:
            id = int(id)
            if id>0:
                return id
            else:
                print('ID must be a positive integer.')
        except ValueError:
            print('ID must be positive integers.')
    
    def validate_age(self, age):
        try:
            age = int(age)
            if age>=0:
                return age
            else:
                print('Age must be a non negative number.')
        except ValueError:
            print('Age must be a non negative number.')
    
    def validate_gender(self, gender):
        if gender not in ('Male', 'Female'):
            print("Gender must be 'Male' or 'Female'.")
        else:
            return gender
    
class Student(Person):
    def __init__(self, name, id, age, gender, stu_id, gpa):
        super().__init__(name, id, age, gender)
        self._stu_id = self.validate_stu_id(stu_id)
        self._gpa = self.validate_gpa(gpa)
    
    def validate_stu_id(self, stu_id):
        if type(stu_id) == str:
            return stu_id
        else:
            print('Student ID must be input of string data type.')
    
    def validate_gpa(self, gpa):
        try:
            gpa = float(gpa)
            if gpa >= 0 and gpa <= 10.0:
                return gpa
            else:
                print('GPA must be a number no less than 0 and no greater than 10')
        except ValueError:
            print('GPA must be a number no less than 0 and no greater than 10')
    
    def get_stu_id(self):
        return self._stu_id
    
    def convert(self):
        gpa = self._gpa
        table1 = {'A+': 9.0, 'A': 8.5, 'B+': 8.0, 'B': 7.0,'C+': 6.5, 'C': 5.5, 'D+':5.5, 'D': 4.5, 'F': 0}
        table2 = {'A+': 4.0, 'A': 4.0, 'B+': 3.5, 'B': 3.0,'C+': 2.5, 'C': 2.0, 'D+':1.5, 'D': 1.0, 'F': 0}
        
        gpa1 = ''
        for i in table1.values():
            while gpa<i:
                break
            if gpa>=i:
                for letter in table1.keys():
                    if table1[letter] == i:
                        gpa1 = letter
                break
        
        gpa2 = table2[gpa1]

        return gpa, gpa1, gpa2
    
n = Student('Ngoc', 139, 19, 'Female', '11214369', 8.9)
n.convert()