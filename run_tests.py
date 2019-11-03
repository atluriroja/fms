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

    def test_create_folder(self):
        """
        This test will create a Commands instance to test the create_folder function.
        Three scenarios are tested here.
            Creation of a folder
            Creation of an existing folder
            Trying to create without folder name
        """
        # timestamp = int(time.time()*1000.0)
        folcommands = Commands("testadmin", "testpwd", "admin")
        expected_results = [
            "Folder created succesfully", "Folder already exists", "Folder creation failed"]
        results = []
        test_vectors = ["create_folder test1",
                        "create_folder test1", "create_folder"]
        results.append(folcommands.create_folder(test_vectors[0]))
        results.append(folcommands.create_folder(test_vectors[1]))
        results.append(folcommands.create_folder(test_vectors[2]))
        print(results)
        if os.path.exists("test1"):
            os.removedirs("test1")
        self.assertListEqual(results, expected_results)

    def test_change_folder(self):
        """
        This test will create a Commands instance to test the create_folder function.
        Three scenarios are tested here.
            Creation of a folder
            Creation of an existing folder
            Trying to create without folder name
        """
        # timestamp = int(time.time()*1000.0)
        folcommands = Commands("testadmin", "testpwd", "admin")
        expected_results = [
            "Folder created succesfully", "Moved to given folder succesfully"]
        results = []
        test_vectors = ["create_folder tmpfol1",
                        "change_folder tmpfol1"]
        results.append(folcommands.create_folder(test_vectors[0]))
        results.append(folcommands.change_folder(test_vectors[1]))
        print(results)
        folcommands.change_folder("change_folder ..")
        if os.path.exists("tmpfol1"):
            os.removedirs("tmpfol1")
        self.assertListEqual(results, expected_results)

    def test_read(self):
        folcommands = Commands("testadmin", "testpwd", "admin")
        expected_results = [
            "The whole file is read , you can try reading again."]
        results = []
        test_vectors = ["read_file newfile.txt"]
        folcommands.write_file("write_file newfile.txt this is a sample")
        # newfile = open("src\\users\\newfile.txt", "w+")
        # newfile.write("This is sample")
        # newfile.close()
        results.append(folcommands.read_file(test_vectors[0]))
        print(results)
        self.assertListEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
