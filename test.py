"""
    Test cases for phoneBook queries
"""
import queries
import unittest


class testQueries(unittest.TestCase):
    """ Test for queries.py"""

    def test_get_user(self):
        login = {'name':'Marc', 'email':'marc@marc.com'}
        queries.register_user(login)
        self.assertTrue(queries.get_user("Marc"))
        queries.delete_User('Marc')
        self.assertFalse(queries.get_user(None))
        self.assertFalse(queries.get_user("1234"))
        self.assertFalse(queries.get_user(""))
        self.assertFalse(queries.get_user(" "))

    def test_register_user(self):
        login = {'name':'Marc', 'email':'marc@marc.com'}
        self.assertTrue(queries.register_user(login))
        queries.delete_User('Marc')
        login['name'] = None
        self.assertFalse(queries.register_user(login))
        """
        self.assertFalse(queries.register_user(""))
        self.assertFalse(quericdes.register_user(" "))
        self.assertFalse(queries.register_user("Marc"))
        self.assertFalse(queries.register_user())
        

    def test_get_user_by_email(self):
        self.assertTrue(queries.get_user_by_email())
        self.assertFalse(queries.get_user_by_email(None))
        self.assertFalse(queries.get_user_by_email(" "))
        self.assertFalse(queries.get_user_by_email("fjsakjfhkjadflajfdhakjdfl"))  # test to make sure email contains@
        self.assertFalse(queries.get_user_by_email("dfasdjkflhkjdd@dsakfjdnetcom"))  # test to make sure email contains either .net or .com

    def test_create_contact(self):
    	self.assertTrue(queries.add_contact("Marc", "marc@marc.com"))
    	self.assertFalse(queries.add_contact(None))
    	self.assertFalse(queries.add_contact(" "))
    	self.assertFalse(queries.add_contact(" ", " "))
    	self.assertFalse(queries.add_contact(""))
    	self.assertFalse(queries.add_contact("", ""))
        self.assertFalse(queries.add_contact())

    def test_delete_contact(self):
    	self.assertTrue(queries.add_contact(""))
        pass

    def test_edit_contact(self):
        pass

    def test_find_by_contacts_name(self):
        pass
        #self.assertTrue(queries.search_by_contacts_name("Marc"))

    def test_find_by_contacts_number(self):
    	pass

    def test_find_by_contacts_email(self):
        pass

    def test_find_contacts_by_address(self):
        pass

    def test_get_users_contacts(self):
    	pass
    """

    def test_delete_user(self):
        self.assertEqual(queries.delete_User(None), None)
        self.assertEqual(queries.delete_User("Tom"), "User not found.")
        login = {'name':'Marc', 'email':'marc@marc.com'}
        queries.register_user(login)
        self.assertEqual(queries.delete_User('Marc'), "user deleted")

if __name__ == "__main__":
	unittest.main()