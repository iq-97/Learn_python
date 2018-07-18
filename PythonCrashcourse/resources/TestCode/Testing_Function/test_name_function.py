import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test's for 'name_function'"""


    def test_first_last_name(self):
        """Do names like 'Janis joplin' work? """
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()