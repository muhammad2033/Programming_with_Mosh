class maaz:
    def python():
        experience = 5
        print(f" he is having {experience} years ")

    def english():
        conversation = 'fluent speaker'
        print(f" he is a {conversation}")

class saad(maaz):
    def pakStudy():
        print("he is having degree of pak study") 

class haris(saad,maaz):
    def scholar():
        print("he is becoming a scholar mashaALLAH ")               

name = maaz
name.english()
name.python()

name = haris
name.english()
name.python()
name.scholar()
name.pakStudy
