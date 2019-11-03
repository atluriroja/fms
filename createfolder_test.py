from src.servercommands import ServerCommands
from src.filecommands import Commands
from src.admincommands import AdminCommands
import unittest
import os


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


if __name__ == "__main__":
    unittest.main()
