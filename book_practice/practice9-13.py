# 练习9-13
from collections import OrderedDict

vocabulary = OrderedDict()

vocabulary['class'] = 'A blueprint for creating objects.'
vocabulary['module'] = 'A file containing Python code.'
vocabulary['exception'] = 'An event that occurs during the execution of a program and disrupts the normal flow of instructions.'
vocabulary['package'] = 'A way to organize related modules.'
vocabulary['decorator'] = 'A function that takes another function as an argument and extends its behavior.'

for word,meaning in vocabulary.items():
    print(word,":",meaning)