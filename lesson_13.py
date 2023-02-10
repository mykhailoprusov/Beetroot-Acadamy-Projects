# Task 1
def func_variables():

    func1 = 123
    func2 = '123'
    func3 = [1,2,3]
    func4 = ('1','2','3')
    func5 = 6

print(func_variables.__code__.co_nlocals)
# Task 2

def func_outside(phrase):

    def func_inside(character):
        print(phrase + character)

    return func_inside

test1 = func_outside('Cheers')

test1('!')

# Task 3
# Я не розумію, чому мій код не працює ...
def choose_func(nums, func1, func2):
    filtration = list(filter(lambda x : True if x > 0 else False, nums)) # а саме оцей фільтер,чомусь
    # не повертає True False
    print(filtration)
    if all(filtration):
        return func1(nums)
    elif not all(filtration):
        return func2(nums)

nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


test_1 = choose_func(nums1,square_nums,remove_negatives)
print(test_1)
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
#
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]