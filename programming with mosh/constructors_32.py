class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        print(f"name is ...{name} ")
        print(f"age is ...{age} ")
    
    def talk(self,name):
        self.name = name
        print(f" {name} is a talkative person:\n")

    def field(self,subject):
        self.subject = subject
        print(f"the subject which i chose i.e,{subject}\n")    

person1 = person('maaz',22)
person1.talk("maaz")
person1.field("Python and English")
        
person2 = person('saad',25)
person2.talk("saad")
person2.field("preaching")

person3 = person('haris',24)
person3.talk("haris")
person3.field("becoming a scholar")
