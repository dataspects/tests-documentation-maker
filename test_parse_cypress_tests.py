import unittest, os
from CypressTestFile import CypressTestFile


class CypressTestFileTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CypressTestFileTest, self).__init__(*args, **kwargs)
        self.name = os.getenv("name")
        self.repository_url = os.getenv("repository_url")
        self.cypress_test_folder = os.getenv("cypress_test_folder")
        self.htmlpreview = os.getenv("htmlpreview")
        self.remote_images_path = os.getenv("remote_images_path")
        self.local_images_path = os.getenv("local_images_path")
        self.tests_doc_html = os.getenv("tests_doc_html")
        self.commands = os.getenv("commands")
        self.commands_html = os.getenv("commands_html")

    def test_tests_doc_html(self):
        for file_path in os.scandir(self.cypress_test_folder):
            ctf = CypressTestFile(
                self.name,
                file_path,
                self.remote_images_path,
                self.local_images_path,
                self.repository_url,
                self.htmlpreview,
            )
            print(ctf.document("python"))
            ctf.save_html_document(self.tests_doc_html)

    def test_list_commands(self):
        CypressTestFile.list_commands(self.commands, self.commands_html)
