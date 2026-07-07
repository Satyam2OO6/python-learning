def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()