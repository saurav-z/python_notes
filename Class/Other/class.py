# class Student:
#     def __init__(self):
#         self.first_name="Hacke"
#         self.last_name="World"
#         self.address="Sifal"
# P=Student()
# print(P.first_name)

# class Student:
#     def __init__(self,fname,lname,addr):
#         self.first_name=fname
#         self.last_name=lname
#         self.address=addr
# A=Student('Hacke','World','Sifal')
# print(A.address)
# B=Student('Neshan','Shrestha','Boudha')
# print(B.first_name,B.last_name,B.address)



# class Dog:
#      def __init__(self, name, color, wt, ht):
#         self.name = name
#         self.color = color 
#         self.weight = wt 
#         self.height = ht

# tiger = Dog("Tiger", "Black", 35, 50) 
# print(f"Name of dog is {tiger.name}. It is of {tiger.color} color and weighs {tiger.weight} kg and it is {tiger.height} inches tall.")






# Define a class student with properties school name , school adress and school telephone no.
# Personal name age adress phone no, with mehod getfullname() and get age() getschoolname(), getschooladress()
class Student:
        school_name="Deerwalk Sifal School"
        school_address="Sifal"
        school_tel="012345678"
        def __init__(self,fn,ln,address,phone,age):
                self.first_name=fn
                self.last_name=ln
                self.address=address
                self.phone=phone
                self.age=age
        def get_fullname(self):
                return f'{self.first_name} {self.last_name}'
        def get_age(self):
                return f'{self.age}'
        @classmethod
        def get_school_name(cls):
                return cls.school_name
        def get_school_address(cls):
                return cls.school_address

S=Student('World','Phuyal','Bhangel','98989898','17')
print(S.get_fullname())
print(S.get_age())
print(S.get_school_name())
print(S.get_school_address())