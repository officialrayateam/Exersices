def print_values(*args, **kwargs):
    print("Args -> ")
    for i in args:
        print(i)

    print("kwargs ->")
    for key, value in kwargs.items():
        print(key, value)


print_values(1, 2, 3, "Hello", name="arshia", yes="no")
