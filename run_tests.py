from src.servercommands import ServerCommands
from src.filecommands import Commands
from src.admincommands import AdminCommands
import unittest
import os


class TestSocket(unittest.TestCase):

    def test_register(self):
        """
        This test will create a ServerCommands instance to authenticate a user.
        Two users will then try to regsitered.
            One admin with valid credentials
            One admin with same credetials
        """
        #timestamp = int(time.time()*1000.0)
        svrcommands = ServerCommands()
        expected_results = [
            "Registered successfully, please login..", "User already exists"]
        results = []
        test_vectors = ["register testadmin testpwd admin",
                        "register testadmin testpwd admin"]
        for test_vector in test_vectors:
            results.append(svrcommands.register(test_vector))
        print(results)
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
        test_vectors = [["testadmin", "testpwd"], ["testuser", "abcd"]]

        for test_vector in test_vectors:
            result = svrcommands.login(test_vector[0], test_vector[1])
            results.append(result['status'])
        self.assertListEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
