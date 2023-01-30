def count_lines(name):
    func = open(name,'r')
    number = func.readlines()
    print('Number of lines is: ',len(number))

def count_chars(name):
    func = open(name,'r')
    number = func.read()
    print('Number of characters is: ',len(number))

def test(name):
    count_lines(name)
    count_chars(name)