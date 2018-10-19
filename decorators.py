import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_run_func():
        print("Before Calling The Actual Function")
        func()
        print("After Calling the Actual Function")
    return function_that_run_func

@my_decorator
def my_function():
    print("This is Actually My Functon")
my_function()
