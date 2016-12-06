"""
    Test cases for phoneBook queries
"""
import queries
import unittest


class testQueries(unittest.TestCase):
    """ Test for queries.py"""

    contacts = {'name':'Marc', 'email':'dklf;ajsd@fjdkjsf.com',
               'phone':'99999999999', 'address':'123 east never never land'}
    
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
        login['name'] = ""
        self.assertFalse(queries.register_user(login))
        #login['name'] = " "
        #self.assertFalse(queries.register_user(login))
        self.assertFalse(queries.register_user("Marc"))
        
    """
    def test_get_user_by_email(self):
        self.assertFalse(queries.get_user_by_email(None))
        self.assertFalse(queries.get_user_by_email(" "))
        self.assertFalse(queries.get_user_by_email(
                         "fjsakjfhkjadflajfdhakjdfl"))  # test to make sure email contains@
        self.assertFalse(queries.get_user_by_email(
                         "dfasdjkflhkjdd@dsakfjdnetcom"))  # test to make sure email contains either .net or .com
    """
    def test_create_contact(self):
        # rewrite to so only having one field filled will pass
        contact = {'name':'', 'email':'','address':'', 'phone':''}
    	self.assertEqual(queries.create_contact(contact), "Invalid input")
    	self.assertFalse(queries.create_contact(None))
        # test if name only
        contact['name'] = 'Bert'
    	self.assertTrue(queries.create_contact(contact))
        # email only
        contact['name'] = ""
        contact['email'] = "jdkflahd@djflskdf.com"
    	self.assertEqual(queries.create_contact(contact), "Invalid input")
    	# address only
        contact['email'] = ""
        contact['address'] = "123 easy street wealth OK"
        self.assertEqual(queries.create_contact(contact), "Invalid input")
    	# phone only
        contact['address'] = ""
        contact['phone'] =  "99999999999"
        self.assertEqual(queries.create_contact(contact), "Invalid input")
        #more than one field filled in
        contact['name'] = "Bob"
        contact['email'] = "uiouepi@uoiupe"
        self.assertEqual(queries.create_contact(contact), "Contact created.")
        queries.delete_contact('Bob')

    def test_delete_contact(self):
        contact = {'name':'Bob', 'phone':'99999999999', 'email':'', 'address':''}
        queries.create_contact(contact)
    	self.assertTrue(queries.delete_contact(""))
        self.assertEqual(queries.delete_contact(None), "Invalid input")
        self.assertEqual(queries.delete_contact(contact['name']),
                         "Contact deleted")
        self.assertEqual(queries.delete_contact('Joe'), "No contact by the name Joe")
    """
    def test_edit_contact(self):
        contact = {'name':'Bob', 'email': 'dkjslaf@hfkdjsa.com',
                   'phone':'', 'address':''}
        queries.create_contact(contact)
        self.assertFalse(queries.edit_contact(None))
        self.assertFalse(queries.edit_contact(""))
        contact['name'] = 'Bobby'
        self.assertEqual(queries.edit_contact(contact),
                         "Contact has been edited.")
        contact['name'] = ""
        contact['email'] = ""
        self.assertEqual(queries.edit_contact(contact), "Invalid entry")
        queries.delete_contact('bob')

    def test_find_contact_by_name(self):
        contact = {'name':'Marc', 'email':'jkflsfjhgjs@dsfjsdk.com',
                   'phone':'', 'address':''}
        queries.create_contact(contact)
        self.assertTrue(queries.find_contact_by_name("Marc"))
        self.assertFalse(queries.find_contact_by_name(None))
        self.assertFalse(queries.find_contact_by_name(""))
        queries.delete_contact('Marc')

    def test_find_contact_by_phonenumber(self):
    	contact = {'name':'Marc', 'email':'dklf;ajsd@fjdkjsf.com',
                   'phone':'99999999999', 'address':''}
        self.assertFalse(queries.find_contact_by_phoneNumber(None))
        self.assertFalse(queries.find_contact_by_phoneNumber(""))
        self.assertFalse(queries.find_contact_by_phoneNumber(contact['phone']))
        queries.create_contact(contact)
        self.assertTrue(queries.find_contact_by_phoneNumber(contact['phone']))
        queries.delete_contact(contact['name'])

    def test_find_contact_by_email(self):
        self.assertFalse(queries.find_contact_by_email(None))
        self.assertFalse(queries.find_contact_by_email(""))
        self.assertFalse(queries.find_contact_by_email(self.contacts['email']))
        queries.create_contact(self.contacts)
        self.assertTrue(queries.find_contact_by_email(self.contacts['email']))
        queries.delete_contact(self.contacts['name'])

    def test_find_contacts_by_address(self):
        self.assertFalse(queries.find_contact_by_address(None))
        self.assertFalse(queries.find_contact_by_address(""))
        self.assertTrue(queries.find_contact_by_address(self.contacts))
        queries.create_contact(contacts)
        self.assertTrue(queries.find_contact_by_address(self.contacts['address']))
        queries.delete_contact(contacts['name'])
    
    
    def test_get_users_contacts(self):
    	login = {'name':'Bob', 'email':'bob@bob.com'}
        self.assertEqual(queries.get_users_contacts(None), None)
        self.assertEqual(queries.get_users_contacts(""), None)
        self.assertTrue(queries.get_users_contacts(login))
        self.assertFalse(queries.get_users_contacts(login['Bob']))
        queries.register_user(login)
        queries.create_contact(self.contacts)
        queries.delete_contact(login['Bob'])
        """
   
    def test_delete_user(self):
        self.assertEqual(queries.delete_User(None), None)
        self.assertEqual(queries.delete_User("Tom"), "User not found.")
        login = {'name':'Marc', 'email':'marc@marc.com'}
        queries.register_user(login)
        self.assertEqual(queries.delete_User('Marc'), "user deleted")

if __name__ == "__main__":
	unittest.main()