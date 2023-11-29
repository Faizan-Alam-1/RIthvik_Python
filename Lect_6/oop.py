# class student:
#     def __init__(self ,name , age):
#         self.name = name
#         self.age =age
  

#     def Namess(self):
#           return f"{self.name} + {self.age}" 
          
        

#     def sum(self,a,b):
#         return a+b     



# # obj 

# student_obj1 = student("Faizan" , 100)
# student_obj2 = student("Ram" , 90)
# student_obj3 = student("sham" ,80)
# print(student_obj1.name)
# print(student_obj1.age)
# print(student_obj2.name)
# print(student_obj2.age)
# print(student_obj3.name)
# print(student_obj3.age)

# # name mtd
# ans  = student_obj1.Namess()
# print(ans)


# # sum mtd
# ans = student_obj.sum(7,4)
# print(ans)


# supper class
class Animal:
     def __init__(self ,  name):
          self.name = name
     def eat(self):
         pass
#     sub class            
class dog(Animal):
     def eat(self , name):
          print(f"eating dog + {name}")
     def brak(self):
          print("bho ,bho")


class cat(Animal):
     def eat(self):
          print("eating cat")
     def mewo(self):
          print("mewo")
               


obj_dog  =  dog("rohan's")

obj_dog.eat()












