import unittest
from city_function import get_full_city_name

class TestCityCase (unittest.TestCase):
    """Test city"""
    def test_format_city_country(self):
        format_city = get_full_city_name('minsk','belarus')
        self.assertEqual(format_city, 'Minsk, Belarus')

    def test_format_city_country_population(self):
        format_name_city=get_full_city_name('minsk','belarus', 30000000)
        self.assertEqual(format_name_city,'Minsk, Belarus - 30000000')