import unittest

test_loader = unittest.defaultTestLoader
test_runner = unittest.TextTestRunner()
test_suite = test_loader.discover('tests', 'Test*.py')

test_runner.run(test_suite)
