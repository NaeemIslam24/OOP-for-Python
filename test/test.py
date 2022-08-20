# class Test():
#     hello = 'this is a test' # it's called class variable
#     # __init__ is called defauld constructor, if it is with parameter it's called parameterized constructor
#     def __init__(self):
     
#         self.name = 'Nayem' # it's called instance variable
#         self.age = 24

#     def update(self): # it's called instance method
#         a=self.age = 20
#         return a
#     def compare(self, other):
#         if self.age == other.age:
#             True
#         else:
#             False

# a1 = Test() # here a1 is an object
# a2 = Test()

# a2.name = 'Tamim'
# a2.age = 36
# if a1.compare(a2):
#     print('They are same')
# else:
#     print('They are different')






# #------------------------------- class variable and instance variable in OOP-----------------------------

# class Car():

#     wheels = 4  # here wheels is called class variable

#     def __init__(self):

#         self.mil = 10    # here self.mil and self.com are called instance variable.
#         self.com = 'BMW'
    
# c1 = Car()
# c1.com = 'TATA'
# print(c1.com)




#  #----------------------------- class method, instance method and static method-----------------------------
# class Student():

#     school = 'Biddakut High School'

#     def __init__(self,m1,m2,m3,m4):

#         self.m1 =m1
#         self.m2 =m2
#         self.m3 =m3
#         self.m4 =m4
    
#     def av(self):  #here av is instance method as it belongs self

#         return (self.m1+self.m2+self.m3+self.m4)/4
#     @classmethod # it's must to define classmethod in class method
#     def info(cls): # here info is class method. it uses cls not self. 
#         return cls.school

#     @staticmethod
#     def nayem(): #here nayem is static method no perameter needed like self and cls
#         print('Nayem is a good student')

# s1 = Student(49,45,89,34)

# print(s1.av())
# print(Student.info())

# Student.nayem()




# #------------------------------- inner class---------------------------

# class Student():

#     school = 'Biddakut High School'

#     def __init__(self,m1,m2,m3,m4):

#         self.m1 =m1
#         self.m2 =m2
#         self.m3 =m3
#         self.m4 =m4
#         self.lap = self.Laptop()



#     class Laptop:

#         def __init__(self):

#             self.cpu = 'i5 8gen'
#             self.ram = 8
#             self.gpu = 4

#         def show(self):
#             return print(self.cpu, self.ram, self.gpu)



# s1 = Student(49,45,89,34)

# s1.lap.show()





# #------------------------------single level inheritance-------------------------

# class A:
#     def feature1(self):
#         print('feather1 is working')
    
# class B(A):
#     def feature2(self):
#         print('feature2 is working')
    

# h = B()
# h.feature1()
# h.feature2()





# #------------------------------multi level inheritance-------------------------

# class A:
#     def feature1(self):
#         print('feather1 is working')
    
# class B(A):
#     def feature2(self):
#         print('feature2 is working')

# class C(B):
#     def feature3(self):
#         print('feature3 is working')
    

# h = C()
# h.feature3()






# #------------------------------multiple inheritance-------------------------

# class A:
#     def feature1(self):
#         print('feather1 is working')
    
# class B():
#     def feature2(self):
#         print('feature2 is working')

# class C(A,B):
#     def feature3(self):
#         print('feature3 is working')
    

# h = C()
# h.feature1()
# h.feature2()
# h.feature3()






# #-----------------------constructor in inheritance--------------------

# class A:
#     def __init__(self):
#         print('hello im init from A class')

# class B(A):

#     def __init__(self):
#         print('hello Im init from B')

# h = B()

# #here both init not called first B init called if not exist, A init will be called.
# # if B init exists, A init wont called. it will stop here.







# #-----------------------constructor in inheritance A and B init call --------------------

# class A:
#     def __init__(self):
#         print('hello im init from A class')

# class B(A):

#     def __init__(self):
#         super().__init__()   # here super represents super class or parent class
#         print('hello Im init from B')

# h = B()

# # here A init and B init both work cause super method is used here






# # ---------------constructor in inheritance A and B init call  multiple inheritance---------------

# class A:
#     def __init__(self):
#         print('hello im init from A class')

# class B:

#     def __init__(self):
       
#         print('hello Im init from B')


# class C(A,B):

#     def __init__(self):
#         super().__init__()    # here A init will be called cause A is left side like C(A,B)
#         print('hello im init from C class')
        

# h = C()



# # ----------------------------------polymorphism duck typing-------------------------------------

# class Pycharm:
#     def execute(self):
#         print('this is a test')


# class Laptop:
#     def code(self, ide):
#         ide.execute()


# ide = Pycharm()
# lap1 = Laptop()

# lap1.code(ide) # here we passed a object inside onther object's method as argument
 

# # ---------------------------------polymorphism operator overloading ----------------------------------

# class Student():
#     def __init__(self, m1, m2):

#         self.m1 = m1
#         self.m2 = m2

#     def __add__(stu1,stu2):
#         m1 = stu1.m1+stu2.m1
#         print('m1 of stu1 and m1 of stu2 addition = ', m1)
#         m2 = stu1.m2+stu2.m2
#         print('m2 of stu1 and m2 of stu2 addition = ', m2)

        
#         sum = Student(m1,m2)
#         return sum
        

# stu1 = Student(39,60)
# stu2 = Student(33,65)

# sum = stu1+stu2     #behind the seen = Student.__add__(stu1,stu2)
# print(sum.m2)


# # ---------------------------------polymorphism method overloading ----------------------------------


#if we have two method with same name it's called method overloading.
#There is no method overloading in python cause we can't define two method with same name.


# # ---------------------------------polymorphism method overriding ----------------------------------


# #--------------second example--------------
# class A:
#     def show(self):

#         print('show is in A')


# class B(A):
#   pass
# s1 = B()
# s1.show()

# #here we call B class but as it has no method it inheritated A class's show method

# #--------------second example--------------


# class A:
#     def show(self):

#         print('show is in A')


# class B(A):
#     def show(self):

#         print('show is in B')

# s1 = B()
# s1.show()

# #here we call B class as it has a method it just worked. it didn't go to A class.
# #  It just override the A class's show method. Method overriding is used a lot

