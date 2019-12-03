"""This module tests read_file function"""
import unittest
from src.filecommands import Commands


class TestFile(unittest.TestCase):
    def test_read_write(self):
        """
        This test will create a Commands instance to test the read_file and write_file function.
        Two scenarios is tested here.
        Create a file with content and Read the file which is created
        """
        folcommands = Commands("testadmin", "testpwd", "admin")
        folcommands.write_file("write_file newfile.txt")
        expected_results = ["The content is written into the file",
                            "\nthis is a sample"]
        results = []
        test_vectors = [
            "write_file newfile.txt this is a sample", "read_file newfile.txt"]
        results.append(folcommands.write_file(test_vectors[0]))
        results.append(folcommands.read_file(test_vectors[1]))
        print(results)
        self.assertListEqual(results, expected_results)


if __name__ == "__main__":
    unittest.main()
