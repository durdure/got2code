class swap:
    def __init__(self,x,y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
print(swap(2, 4))

