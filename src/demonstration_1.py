"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here

#     new_string = ""

#     for i in string:
#         if ord(i) > 65 or ord(i) < 90:
#            new_string += chr(ord(i) + 32)
#         else: 
#             new_string += i

#     return new_string

# print(to_lower_case("LLAMA"))

    return ''.join([chr(ord(c) + 32) if ord(c) > 64 and \
    ord(c) < 91 else c for c in string])