import random
# Task 1
def bubble_down(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if list_a[i] < list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

def bubble_up(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a


print(bubble_down([4,8,1,14,8,2,9,5,7,6,6]))
print(bubble_up([4,8,1,14,8,2,9,5,7,6,6]))

# Task 2
# Не осилив. І відоси дивився,і з chatgpt розмовляв,але так і не зміг збагнути, як рекурсія не тільки ділить
# наш список на маленькі списки з одним елементом,а ще й сортує їх,коли збирає у великий список назад


# Task 3

def quick_sort(sequence):
    length = len(sequence)
    if length < 100:
        if length <= 1:
            return sequence

        comparison = sequence.pop()

        greater = []
        less = []

        for i in sequence:
            if i > comparison:
                greater.append(i)

            else:
                less.append(i)

        return quick_sort(less) + [comparison] + quick_sort(greater)
    elif length >= 100:
        length_ = range(1,length)
        for i in length_:
            comparison = sequence[i]

            while sequence[i-1] > comparison and i > 0:
                sequence[i], sequence[i-1] = sequence[i-1],sequence[i]
                i-=1

        return sequence

if __name__ == '__main__':
    print(quick_sort([random.randint(0, 500) for _ in range(1000)]))
    print(quick_sort([random.randint(0, 500) for _ in range(10)]))

    # insertion sort буде швидшим в обчисленні великих списків,бо швидкий сорт створюватиме багато лістів.
    # quick_sort(less) + [comparison] + quick_sort(greater) кожен раз,коли будемо викликати рекурсію, там створю-
    #ватимуться нові списки потім ця рекурсія викличе ще рекурсії,які в свою чергу також створять списки.