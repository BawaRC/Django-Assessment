"""
Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}
"""
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield the length in the specified format
        yield {'length': self.length}
        # Then yield the width in the specified format
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 5)

# Iterate over the instance
for attribute in rect:
    print(attribute)


"""Explanation - 

Initialization: The Rectangle class is initialized with two parameters: length and width, both of which are integers.

Iteration with __iter__: The __iter__ method is defined to allow iteration over the instance. The method uses yield to first return the length in the required format ({'length': <value>}) and then the width ({'width': <value>}).

Output Example:
    {'length': 10}
    {'width': 5}

This implementation meets the requirements by making the Rectangle class both iterable and able to yield its length and width in the specified format.
"""