import queries
import unittest

#def test_add_user():
#	assert queries.add_user(None)
#	assert queries.add_user("")  # should fail
#	assert queries.add_user(" ")  # should fail
#	assert queries.add_user("Marc")  # should pass
#	assert queries.add_user("Marc")  # Should fail

#def test_get_user():
#    assert queries.get_user("Marc")
#    assert queries.get_user(None)
#    assert queries.get_user(" ")

class testQueries(unittest.TestCase):
    """ Test for queries.py"""

    def test_get_user(self):
        self.assertTrue(queries.get_user("Marc"))
        self.assertFalse(queries.get_user(None))
        self.assertFalse(queries.get_user("1234"))
        self.assertFalse(queries.get_user(""))
        self.assertFalse(queries.get_user(" "))

    def test_register_user(self):
    	self.assertTrue(queries.register_user("Marc", "marc@marc.com"))
    	self.assertFalse(queries.register_user(None))
    	self.assertFalse(queries.register_user(""))
    	self.assertFalse(queries.register_user(" "))
    	self.assertFalse(queries.register_user("Marc"))
        self.assertFalse(queries.register_user())

    def test_get_user_by_email(self):
        self.assertTrue(queries.get_user_by_email())
        self.assertFalse(queries.get_user_by_email(None))
        self.assertFalse(queries.get_user_by_email(" "))
        self.assertFalse(queries.get_user_by_email("fjsakjfhkjadflajfdhakjdfl"))  # test to make sure email contains@
        self.assertFalse(queries.get_user_by_email("dfasdjkflhkjdd@dsakfjdnetcom"))  # test to make sure email contains either .net or .com


if __name__ == "__main__":
	unittest.main()