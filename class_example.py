class my_class ():
    def __init__ (self, greet= "lion"):
        self.greet = greet
    
    def __repr__ (self):
        return "a custom object (%r)" % (self.greet)

a = my_class();
print (a)