# -*- coding: utf-8 -*-
import random

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.message = self.name+"の年齢は"+str(self.age)+"なので"
    
    def check_adult(self):
        if self.age >= 20:
            return self.message+"大人です"
        else:
            return self.message+"大人ではありません"

# Humanクラスのインスタンスを複数(10回)生成してリストに追加
human_array = [Human("侍太郎"+str(i+1),random.randint(0,100)) for i in range(10)]

# 要素数分check_adultメソッド実行
for human in human_array:print(human.check_adult())

