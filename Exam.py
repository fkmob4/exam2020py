# Copyright 2020 by Michael Fedoruk, Taras Shevchenko National University of Kyiv
# All rights reserved.
# This file is part of the DevOps exam2020
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.


import copy
import unittest

def sum(a0, d, n):
    if n == 1:
        return a0
    else:
        return a0 + (n-1) * d + sum(a0, d, n-1)
n=int(input("Введіть N "))
k=int(input("Введіть крок "))
first=int(input("Введіть перший член "))
print('Сума прогресії: ') 
print (sum(first, k, n))

class MyTest(unittest.TestCase): #створення класу для реалізації тестів
    def test_usage1(self):#створення функції для тесту
        self.assertIsNot(n, sum(first, k, n))        
    def test_div(self):
        self.assertEqual(sum(first, k, n))
if __name__ == "__main__":
    unittest.main()#команда яка запускає всі тести із заданого модуля








