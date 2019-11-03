"""This module tests read_file function"""
import unittest
from src.filecommands import Commands


def test_read(self):
    """
    This test will create a Commands instance to test the read_file function.
    Three scenarios are tested here.
        Read the file which is created
    """
    folcommands = Commands("testadmin", "testpwd", "admin")
    expected_results = [
        "The whole file is read , you can try reading again."]
    results = []
    test_vectors = ["read_file newfile.txt"]
    folcommands.write_file("write_file newfile.txt this is a sample")
    results.append(folcommands.read_file(test_vectors[0]))
    print(results)
    self.assertListEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
