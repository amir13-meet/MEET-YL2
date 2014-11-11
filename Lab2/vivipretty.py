class Animal():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def sleep(self):
		print self.name+" is "+str(self.age)+" years old, and is sleeping now."

	def eat(self,food):
		print self.name+" is now eating "+food

#-----------------------------------------------

class Bird(Animal):
	Animal.__init__(self,name,age,w_color):
		self.w_color = w_color

	def fly(self):
		self.name+" with "+self.w_color+" color wings is flying"

#-----------------------------------------------

class Dog(Animal):
	Animal.__init__(self,name,age):

	def bark(self):
		self.name+" is barking"

#-----------------------------------------------

l = Dog("Lucky",4)
l.bark()

c = Bird("Stacy",1,"Blue")
c.fly()