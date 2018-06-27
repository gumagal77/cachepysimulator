#from Cache import*
class Animal:
    def __init__(self):
        self.n = 1
    def run(self):
        print('correndo')
    def move(self):
        self.run()

class Peixe(Animal):
    def __init__(self):
        super().__init__()
        self.n = 2
        
    def run(self):
        print("nadando")

m = Peixe()
m.move()

#m = Cache(1,1,1)
print(m)
