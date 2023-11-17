glossary = {
    'string' : 'a sequence of characters',
    'integer' : 'a whole number',
    'function' : ' group of related statements that performs a specific task',
    'list' : 'a data structure in Python that is a mutable, or changeable, ordered sequence of elements',
    'comment' : 'the inclusion of short descriptions along with the code to increase its readability',
    'float' : 'floating point number',
    'boolean' : 'used to represent the truth value of an expression',
    'value' : 'basic things a program works with. such as a letter or a number',
    'variable' : 'a symbolic name that is a reference or pointer to an object',
    'loop' : 'repeating something over and over until a particular condition is satisfied.'
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)