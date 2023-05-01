import asyncio
import math
import multiprocessing

list_fibonacci = []
list_factorial = []
list_square = []
list_cube = []

async def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        list_fibonacci.append(fib[n])

async def factorial(n):
    num = math.factorial(n)
    list_factorial.append(num)

async def squares(n):
    list_square.append(n**2)

async def cube(n):
    list_cube.append(n**3)

async def main():
    for i in range(1,11):
        task1 = asyncio.create_task(fibonacci(i))
        task2 = asyncio.create_task(factorial(i))
        task3 = asyncio.create_task(squares(i))
        task4 = asyncio.create_task(cube(i))

        await asyncio.gather(task1,task2,task3,task4)

asyncio.run(main())

print(list_fibonacci)
print(list_factorial)
print(list_square)
print(list_cube)


manager = multiprocessing.Manager()
list_fibonacci2 = manager.list()
list_factorial2 = manager.list()
list_square2 = manager.list()
list_cube2 = manager.list()

processes = []
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        list_fibonacci2.append(fib[n])

def factorial2(n):
    num = math.factorial(n)
    list_factorial2.append(num)

def squares2(n):
    list_square2.append(n**2)

def cube2(n):
    list_cube2.append(n**3)


if __name__ == '__main__':
    manager = multiprocessing.Manager()

    list_fibonacci2 = manager.list()
    list_factorial2 = manager.list()
    list_square2 = manager.list()
    list_cube2 = manager.list()

    processes = []

    for i in range(1,11):
        process1 = multiprocessing.Process(target=fibonacci2,args=(i,list_fibonacci2,))
        process2 = multiprocessing.Process(target=factorial2,args=(i,list_factorial2,))
        process3 = multiprocessing.Process(target=squares2,args=(i,list_square2,))
        process4 = multiprocessing.Process(target=cube2,args=(i,list_cube2,))

        processes.append(process1)
        processes.append(process2)
        processes.append(process3)
        processes.append(process4)

    for i in processes:
        i.start()

    for i in processes:
        i.join()

    print(list_fibonacci2)

#####  Я не можу знайти помилку...