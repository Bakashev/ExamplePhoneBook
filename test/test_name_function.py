import unittest
from name_funcation import get_formated_name

class NameTestedCase (unittest.TestCase):
    """Test for name_function.py"""
    def test_first_last_name (self):
        """names Jonis Joplin work correct"""
        formated_name=get_formated_name('joins','joplin')
        self.assertEqual(formated_name, 'Joins Joplin')

    def test_firs_last_midle_name(self):
        """names Jonis Joplin Jone work correct"""
        full_name=get_formated_name('jonis','joplin','jone')
        self.assertEqual(full_name,'Jonis Joplin Jone')


