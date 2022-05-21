"""
HW 5
4** Amazon interview question:
Create a function that will take a string as an input and return the 1st unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

How to handle ""? => return Value Error
"""


# def unique(string: str):
#     # Google
#     string = string.lower()  # google
#
#     for l in string: # O(n)  # l => 1
#         if string.count(l) == 1:  # O(n)
#             return l
    # O(n^2)
#
# print(unique('Google'))
# print(unique('Amazon'))

def unique(string: str):
    string = string.lower()  # amazon
    d = {}

    for letter in string:   # O(n)
        if letter not in d:
            d[letter] = 1  # d = {'a': 1, 'm': 1}
        else:
            d[letter] += 1 # d = {'a': 2, 'm': 1}

    print(d)

    for k, v in d.items():  # O(n)
        if v == 1:
            return k


    # O(n)

# print(unique('Goog'))
print(unique('Amazon'))
print(unique(''))
print(unique('nnnnnn'))
print(unique('Amazon'))
print(unique(251432514))