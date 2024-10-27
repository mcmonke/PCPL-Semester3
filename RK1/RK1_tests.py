import unittest
from RK1_refactoring import task_a1, task_a2, task_a3, libraries, languages

class TestLibraryFunctions(unittest.TestCase):
    def test_task_a1(self):
        result = task_a1(libraries, languages)
        expected_result = [
            ('Python', 10, 'Библиотека алгоритмов'),
            ('JavaScript', 8, 'Библиотека анализа данных'),
            ('Java', 7, 'Библиотека веб разработки'),
            ('C++', 6, 'Библиотека веб разработки'),
            ('R', 5, 'Библиотека веб разработки')
        ]
        self.assertEqual(result, expected_result)
        
    def test_task_a2(self):
        result = task_a2(libraries, languages)
        expected_result = [
            ('Библиотека анализа данных', 8),
            ('Библиотека веб разработки', 18),
            ('Библиотека алгоритмов', 10)
        ]
        # Сортировка для игнорирования порядка
        self.assertEqual(sorted(result), sorted(expected_result))

    def test_task_a3(self):
        result = task_a3(libraries, languages)
        expected_result = {
            'Библиотека веб разработки': ['Java', 'C++', 'R'],
            'Библиотека мобильной разработки': ['Python']
        }
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
