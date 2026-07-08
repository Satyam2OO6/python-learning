def decorator(func):

    def wrapper(name):
        print("Starting...")

        func(name)

        print("Finished.")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Alice")