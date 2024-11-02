def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function()

my_test_func = test_function

my_test_func()

my_inner_func = inner_function()