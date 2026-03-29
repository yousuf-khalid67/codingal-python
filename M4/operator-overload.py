class Programer:
    def __init__(self, name, experience):
        self.experience=experience
        self.name=name
    
    
    def __lt__(self, other):
        if self.experience<other.experience:
            return True 
        else:
            return False
        



programer1=Programer("Mimi",0.5)
programer2=Programer("Bob",2)
if programer1<programer2:
    print(f"{programer2.name} has more experience than {programer1.name}")

else: 
     print(f"{programer1.name} has more experience than {programer2.name}")
    