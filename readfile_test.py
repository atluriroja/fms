from src.servercommands import ServerCommands
from src.filecommands import Commands
from src.admincommands import AdminCommands
import unittest
import os


def test_read(self):
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
