"""This module tests change_folder function"""
import unittest
import os
from src.filecommands import Commands


class ChangeFolder(unittest.TestCase):
    def test_change_folder(self):
        """
        This test will create a Commands instance to test the change_folder function.
        Three scenarios are tested here.
            Creation of a folder
            Changing to the created folder
        """

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


if __name__ == "__main__":
    unittest.main()
