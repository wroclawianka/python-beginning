def increment0(number, by):
    return (number, number + by)


def increment1(number, by=1):  # default value
    return (number, number + by)


def increment(number: int, by: int = 1) -> tuple:  # types inting (int, int, -> tuple)
    return (number, number + by)


# PEEP-8: afer functiion two emply lines
result = increment0(2, 3)
print(result)  # (2, 5)

# key-word argument, to make it more readable
result = increment0(2, by=3)

result1 = increment(2)  # with default value
