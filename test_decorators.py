import lesson_14_
import unittest

class DecoratorsTestCase(unittest.TestCase):

    def test_add_decorator(self):

        sum = lesson_14_.add(2,2,2,4,9)
        sum1 = lesson_14_.add(0,0,0)
        sum2 = lesson_14_.add(2)
        sum3 = lesson_14_.add(-2,2,2,4,-9)
        sum4 = lesson_14_.add(-2,-2,-2,-4,-9)
        sum5 = lesson_14_.add(1000,10000,0,2)

        self.assertEqual(sum,19)
        self.assertEqual(sum1,0)
        self.assertEqual(sum2,2)
        self.assertEqual(sum3,-3)
        self.assertEqual(sum4,-19)
        self.assertEqual(sum5,11002)

    @unittest.skip('Demostrating testing')
    def test_stop_words_create_slogan_(self):
        name1 = lesson_14_.create_slogan_('Steve')

        self.assertEqual(name1,'Steve drinks * in his brand new *!')

        raise ZeroDivisionError()

    def test_arg_rules_create_slogan(self):
        name1 = lesson_14_.create_slogan('S05eve@')

        self.assertEqual(name1,'S05eve@ drinks pepsi in his brand new BMW!')


        self.assertRaises(ValueError,lesson_14_.create_slogan,'S05eve')





