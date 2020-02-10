class Person:


    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        print("Hello, my name is",self.name,"and I am",self.age,"years old. My interests are",self.interests)


person = Person('Ryan',30,'male','being a hardarse,agile and ssd hard drives')
greeting = person.hello()
print(greeting)
