import unittest

test_loader = unittest.defaultTestLoader
test_runner = unittest.TextTestRunner()
test_suite = test_loader.discover('tests', 'Test*.py')

test_result = test_runner.run(test_suite)
if test_result.failures or test_result.errors:
    exit(1)
