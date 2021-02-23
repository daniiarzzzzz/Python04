name = "Daniiar"
age = 21


def function(func):  # Callback
    a = func()
    return a


def function2():
    return "LOl"


a = function
print(a(function2))
print(function(function2))
