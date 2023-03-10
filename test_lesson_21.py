import lesson_21
import unittest

class OpenFileTestCase(unittest.TestCase):

    def test_writing_reading(self):
        with lesson_21.OpenFile('example.txt', 'w') as f:
            f.write('abcd. I love OOP. No. ')

        with lesson_21.OpenFile('example.txt', 'r') as poo:
            result = poo.read()
            self.assertEqual(result,'abcd. I love OOP. No. ')

    def test_writing_appending(self):
        with lesson_21.OpenFile('example.txt', 'w') as poo:
            poo.write('I have no idea what I should write here ')

        with lesson_21.OpenFile('example.txt', 'a') as poo:
            poo.write('But')


        with lesson_21.OpenFile('example.txt', 'r') as poo:
            result = poo.read()
            self.assertEqual(result,'I have no idea what I should write here But')

# Я гадки не маю,які нормальні тести можна написати для цього контекстного менеджера...
