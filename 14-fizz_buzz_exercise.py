# solved by myself

def fizz_buzz(input):
    result = ""
    if input % 3 == 0:
        result += "Fizz"
    if input % 5 == 0:
        result += "Buzz"
    if(result == ""):
        result = input
    return result


print(fizz_buzz(7))
