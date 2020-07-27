class Robot:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def reset(self):
        print("Hello, my name is " + self.name)


    

r1  = Robot("AB123",1)
r1.reset()
