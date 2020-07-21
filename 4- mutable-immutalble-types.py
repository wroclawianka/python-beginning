# IMMUTABLE
x = 1
id(x)  # adress of memory location
x = x + 1
# new memory alocated (new address)

# MUTABLE
y = [1, 2, 3]
y.append(4)
# new memeory NOT slocated, you can check with id(y)
