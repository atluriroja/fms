"""
This file contains the tests given for assignment 3.
Each of these tests must pass for your assignment to be assessed for the commands
register, login and delete.

The following unit tests are conducted on the class Snake:
    1. test_register
        This test will register a user.
        Two commands will then be created.
                One with valid user details
                One with existing user details

    2. test_login
        This test will create a ServerCommands instance to authenticate a user.
        Two users will then be logged in.
            One user with valid credentials
            One user with invalid credetials

    3. test_delete
        This test will create a ServerCommands instance to authenticate a user.
        Two users will then be logged in.
            One user with valid credentials
            One user with invalid credetials
"""
import unittest
import time
from src.servercommands import ServerCommands
from src.admincommands import AdminCommands
class TestCommands(unittest.TestCase):
    """
    A simple structure for  Test cases.

    Attributes:
    -----------------

    Methods:
    -----------------
        test_register(command):
            Used to test register command

        test_login(user_name, password):
            Used to test login command

        test_delete(user_name, password):
            Used to test login command
    """
    def test_register(self):
        """
        This test will create a ServerCommands instance to authenticate a user.
        Two users will then try to regsitered.
            One admin with valid credentials
            One admin with same credetials
        """
        svrcommands = ServerCommands()
        expected_results = [
            "Registered successfully, please login..", "User already exists"]
        results = []
        milliseconds = int(round(time.time() * 1000))
        test_vectors = ["register testadmin"+str(milliseconds)+" testpwd admin",
                        "register testadmin testpwd admin"]
        for test_vector in test_vectors:
            results.append(svrcommands.register(test_vector))
        self.assertListEqual(results, expected_results)

    def test_login(self):
        """
        This test will create a ServerCommands instance to authenticate a user.
        Two users will then be logged in.
            One user with valid credentials
            One user with invalid credetials
        """
        svrcommands = ServerCommands()
        expected_results = ["Success", "Failure"]
        results = []
        test_vectors = [["testadmin", "testpwd"], ["testxxx", "abcd"]]

        for test_vector in test_vectors:
            result = svrcommands.login(test_vector[0], test_vector[1])
            results.append(result['status'])
        self.assertListEqual(results, expected_results)

    def test_delete(self):
        """
        This test will create Admin Commands instance to delete a user.
        Two users will then be deleted.
            One valid user
            One with invalid user
        """
        expected_results = ["Successfully deleted the user", "User doesn't not exists"]
        results = []
        svrcommands = ServerCommands()
        svrcommands.register("register testdeluser testpwd admin")
        admincommands = AdminCommands("testadmin", "testpwd", "admin")
        test_vectors = ["testdeluser", "testdeluser"]

        for test_vector in test_vectors:
            results.append(admincommands.delete(test_vector))
        self.assertListEqual(results, expected_results)

if __name__ == "__main__":
    unittest.main()
