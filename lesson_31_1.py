import multiprocessing
from math import sqrt

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]

def prime(n,queue):
    prime_flag = 0
    if (n > 1):

        for i in range(2, int(sqrt(n)) + 1):

            if (n % i == 0):
                prime_flag = 1
                break

        if (prime_flag == 0):
            queue.put((n,True))

        else:
            queue.put((n,False))
    else:
        queue.put((n,False))


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    processes = []

    for i in NUMBERS:

        process = multiprocessing.Process(target=prime, args=(i, queue))
        process.start()
        processes.append(process)

    for i in processes:
        i.join()

    while not queue.empty():
        n, is_prime = queue.get()
        print(f"{n}: {is_prime}")






