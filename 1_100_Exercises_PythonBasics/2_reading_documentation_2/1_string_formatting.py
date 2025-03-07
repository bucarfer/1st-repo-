'''Python offers multiple ways to format strings. The str.format method is a popular method, but since Python 3.6, a new way called f-strings (formatted string literals) was introduced. F-strings offer a concise way to embed expressions inside string literals.
Given the following variables:
name = "Victor"
profession = "programmer"

How can you print the string Hello, Victor. You are a programmer. using the str.format method? You should fill in the name and profession in a string literal that contains the rest of the text.
How can you achieve the same result using an f-string?
Refer to the Python documentation on Format String Syntax and Formatted string literals for guidance.
'''

name = "Victor"
profession = "programmer"

# using strings 
print ('hello', name, 'you are a', profession,'.')
# using str.format
message = 'hello {} you are a {}.'
print(message.format(name,profession))
# using f-string
print (f'hello {name} you are a {profession}.')