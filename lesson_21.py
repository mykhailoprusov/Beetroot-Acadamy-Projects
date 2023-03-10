# Task 1
import logging

logging.basicConfig(filename='openfile_logging.log',level=logging.INFO)

class OpenFile:
    counter = 0
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):

        OpenFile.counter +=1
        logging.info(f'Running {self.__class__.__name__} with filename:{self.filename} and mode: {self.mode}')
        try:
            self.file = open(self.filename,self.mode)
            return self.file
        except FileNotFoundError:
            print(f'No such file or directory: {self.filename}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':
    with OpenFile('example.txt','w') as f:
        f.write('abcd. I love OOP. No. ')

