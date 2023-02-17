# Task 1
import functools

def adder_decorator(func):
    def wrapper(*args):
        func(*args)
    return wrapper

@adder_decorator
def add(*args):
    x = functools.reduce(lambda x,y: x+y,args)
    print(x)

add(5,3,2,7,1)

# Task 2

def stop_words(words):
    def decorator_func(func1):
        def wrapper(first_name):
            print('Original func before executing')
            result = func1(first_name)
            print('After executing')
            for i in words:
                if i in result:
                    result = result.replace(i,'*')
            print(result)
            return result
        return wrapper
    return decorator_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('Steve')

# Task 3

def arg_rules(type_, max_length, contains):
    def decorator(func_orig):
        def wrap(first_name):
            lst = [1 if x in first_name else 0 for x in contains]

            if isinstance(first_name,type_) and len(first_name) <= max_length and all(lst):
                return func_orig(first_name)
            else:
                return False
        return wrap
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('S05eve@'))

# assert create_slogan('johndoe05@gmail.com') is False
# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'


# def wrapper(word):
#     lst = [1 if x in word else 0 for x in contains]
#
#     if isinstance(word,type_) and len(word) <= max_length and all(lst):
#         return func(word)
#     else:
#         return False