import unittest
from tests.test_save_book_details import SaveBookDetails

# Loads the Class which we want to test
test = unittest.TestLoader().loadTestsFromTestCase(SaveBookDetails)

# Test Suite is used to run a number of test cases at once in the order which we give
executor = unittest.TestSuite([test])

# Actual Execution of our test will take place here
unittest.TextTestRunner(verbosity=2).run(executor)
