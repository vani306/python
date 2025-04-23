class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, String):
            self.value += other.value
        else:
            self.value += str(other)
        return self
    
    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def display(self):
        print(self.value)

s1 = String("Hello")
s2 = String("World") 

s1 += s2
s1.display()  

s1.toLower()
s1.display()  

s1.toUpper()
s1.display()  
