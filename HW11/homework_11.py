from datetime import datetime


class ContextManager:
    def __enter__(self):
        print("="*10)
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None and exc_type is None and exc_val is None:
            print("=" * 10)
        else:
            print(exc_type)
            print(exc_val)
            print(exc_tb)
            print("=" * 10)
            return True


with ContextManager():
    print(1/0)

    def name_time_decorator(func):
        def inner1(*args, **kwargs):
            print(f"Function {func.__name__} started at {datetime.now()}")
            func(*args, **kwargs)
        return inner1


    @name_time_decorator
    def multiply_two(num):
        print(num * 2)


    result = multiply_two


    class MyCustomException(Exception):
        def __init__(self, message):
            self.message = message


    inp = input("Input some integer:")

    try:
        if not inp.isdigit():
            raise MyCustomException("Custom exception is occurred")
    except MyCustomException as exc:
        print(exc)
    print("smth else")

try:
    print("="*10)
    result(5)
except NameError:
    print("Seems like name is not found")
else:
    print("Here is your result!")
finally:
    print("Thanks for using this func!")
    print("="*10)