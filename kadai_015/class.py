# -*- coding: utf-8 -*-

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age        
    
    def printinfo(self):
        print(self.name, self.age)

name:str = "侍太郎"
age:int  = 30
human = Human(name,age)
human.printinfo()
