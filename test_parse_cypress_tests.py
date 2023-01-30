import unittest, os, sys, cairo
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
        self.doc_folder_path = os.getenv("doc_folder_path")
        self.commands = os.getenv("commands")
        self.commands_html = os.getenv("commands_html")

    def test_doc_folder_path(self):
        self._annotate_screenshots()
        self.promptForUserConfirmation()
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
            ctf.save_html_document(self.doc_folder_path+ctf.file_name()+".html")
            print("See file://"+self.doc_folder_path)

    def test_list_commands(self):
        CypressTestFile.list_commands(self.commands, self.commands_html)

    def promptForUserConfirmation(self, resp=False):
        print("Did you run all the Cypress tests in "+self.cypress_test_folder+" ? (y/n)")
        answer = input()
        if answer != "y":
            sys.exit()

    def _annotate_screenshots(self):
        for file_path in os.scandir(self.local_images_path):
            url = self.local_images_path+"/"+file_path.name
            
            comps = os.path.basename(file_path.name).split("__")
            if len(comps) > 1:
                final_filename = comps[0]+".png"
                surroundings_frame_factor = int(comps[1].replace(".png", "")) + 80
                
                screenshot = cairo.ImageSurface.create_from_png(url)
                screenshot_height = screenshot.get_height()
                screenshot_width = screenshot.get_width()
                
                element_height = screenshot_height - surroundings_frame_factor
                element_width = screenshot_width - surroundings_frame_factor

                pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
                pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.3)

                ctx = cairo.Context(screenshot)
                ctx.rectangle(
                    surroundings_frame_factor / 2,
                    surroundings_frame_factor / 2,
                    element_width,
                    element_height
                )

                ctx.set_source(pat)
                ctx.fill()
                os.remove(url)
                screenshot.write_to_png(self.local_images_path+"/"+final_filename)