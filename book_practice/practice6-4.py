# 练习6-4
vocabulary = {
    'list': 'A collection of items stored in a specific order.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A block of code that performs a specific task.',
    'loop': 'A way to repeat a block of code multiple times.',
    'variable': 'A named storage location for data.'
}
for word,meaning in vocabulary.items():
    print(word,":",meaning)

vocabulary['class'] = 'A blueprint for creating objects.'
vocabulary['module'] = 'A file containing Python code.'
vocabulary['exception'] = 'An event that occurs during the execution of a program and disrupts the normal flow of instructions.'
vocabulary['package'] = 'A way to organize related modules.'
vocabulary['decorator'] = 'A function that takes another function as an argument and extends its behavior.'
for word,meaning in vocabulary.items():
    print(word,":",meaning)