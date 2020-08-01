letters = ["a", "b", "c", "d"]
zeros = [0] * 100  # [0, 0, 0, 0, 0...]
# conbined = zeros + letters
numbers = list(range(20))  # [0, 1, 2, 3, 4...]
chars = list("Hello")  # ['H', 'e', 'l', 'l', 'o']


# accessing items
print(letters[0::2])    # every second element -> ["a", "c"]
print(range(20)[::2])   # every odd element [0, 2, 4, 6, ...]
print(range(20)[::-1])  # reverse order


# list unpacking
numbers = [1, 2, 3]
first, second, third = numbers
# first, second = numbers ## Error
first, second, *other = numbers  # list other will be created with value [3]

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *other, last = numb
print(first, last)
print(other)


# looping + unpacking

# for letter in enumerate(letters):
#     print(letter)  # tuple with index and value

for index, letter in enumerate(letters):
    print(index, letter)


# add / remove item
letters = ["a", "b", "c", "d"]
letters.append("e")
letters.insert(0, "-")

letters.pop(0)
letters.remove('b')  # first occurence only
del letters[0:3]     # range
letters.clear()      # all elements

# finding
letters.index("d")
letters.count("d")   # number of occurences
# letters.index("x") # error
# do:
if "d" in letters:
    i = letter.index("d")
