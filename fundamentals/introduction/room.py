# Class, static, methods ROUPS

class Room:

    def __init__(self,size,name,type):
        self.name = name
        self.size = size
        self.type = type

    def __repr__(self) -> str:
        return f"{self.name} | {self.type}"
    
    def info(self): -> None:
        print(f"name: {self:name}")
        print(f"size: {self:size}")
        print(f"type: {self:type}")

r1 = Room(20,"Tyler's Bedroom","Bedroom")
r2 = Room(10, "Hallway closet", "closet")

print (r1)
print (r2)
