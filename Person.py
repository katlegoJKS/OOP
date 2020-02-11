class Person:


    def __init__(self,name,age,gender,interests=[]):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        interests = ",".join(self.interests)
        return "Hello, my name is {} and I am {} years old. My interests are {} ".format(self.name,self.age,interests)


person = Person("Ryan",30,"male",["being a hardarse,agile and ssd hard drives"])
print(person.hello())
