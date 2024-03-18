# -*- coding: utf-8 -*-
"""
上辺：10cm
下辺：20cm
高さ：5cm

公式：台形の面積 =（上辺＋下辺）× 高さ ÷ 2
"""

#上辺
top_edge:int = 10

#下辺
bottom_edge:int = 20

#高さ
height:int = 5

#公式
area:int = (top_edge + bottom_edge) * height / 2

#表示
print(str(area)+"cm²")
