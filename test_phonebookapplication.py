import phonebook
import unittest

class PhoneBookTestCase(unittest.TestCase):


    def tearDown(self) -> None:

        with open('phonebook_application_data.json', 'w') as data:
            new_data = phonebook.json.dumps(phonebook.users)
            data.write(new_data)

    def test_first_name_search(self):

        result = phonebook.first_name_search('john')
        self.assertEqual(result,['john wark, phone number:+380888341677, city:london'])

        result1 = phonebook.first_name_search('josh')
        self.assertEqual(result1,None)

    @unittest.skip
    def test_delete_record(self):

        result = phonebook.delete_record('+440765332156')
        self.assertEqual(result,'You successfully deleted the record!')

    @unittest.skip
    def test_update_record(self):

        result = phonebook.update_record("+440765332199")
        self.assertEqual(result,'You successfully updated info!')

    def test_second_name_search(self):

        result = phonebook.second_name_search('WARK')
        self.assertEqual(result,['john wark, phone number:+380888341677, city:london'])

        result1 = phonebook.second_name_search('KAFKA')
        self.assertEqual(result1,None)

    def test_full_name_search(self):

        result = phonebook.full_name_search('john','wark')
        self.assertEqual(result,['john wark, phone number:+380888341677, city:london'])

        result1 = phonebook.full_name_search('josh','kaguja')
        self.assertEqual(result1,None)

    def test_city_search(self):

        result = phonebook.city_search('glasgow')
        self.assertEqual(result,['emerald pobg, phone number:+440765332199, city:glasgow','will borsh, phone number:'
                                '+440765332156, city:glasgow'])

        result1 = phonebook.city_search('kyiv')
        self.assertEqual(result1,None)






