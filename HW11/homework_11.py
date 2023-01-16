import time
from datetime import datetime


class ContextManager:
    def __enter__(self):
        print("="*10)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("="*10)


with ContextManager():
    try:
        def name_time_decorator(func):
            def inner1(*args, **kwargs):
                print(f"Function {func.__name__} started at {datetime.now()}")
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                print(f"Function {func.__name__} take  {end_time - start_time}")
            return inner1


        @name_time_decorator
        def multiply_two(num):
            print(num * 2)

        multiply_two(5)

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
    except Exception as error:
        print(error)



