def multiply(*list):
    print(list)  # py treat *list as tuple
    # return a* b


multiply(2, 3, 4, 5)


def save_user(**user):  # dictonary
    print(user)


save_user(id=1, name='Dorota')
