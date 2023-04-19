import threading

class Counter(threading.Thread):
    counter = 0
    rounds = 100_000
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(Counter.rounds):
            Counter.counter +=1


if __name__ == '__main__':
    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(Counter.counter)

    # Our threads are virtually separate one from another and execute their code separately but since they
    # have a shared variable counter,they both add 100_000 to that variable and the result is consequently 200_000

