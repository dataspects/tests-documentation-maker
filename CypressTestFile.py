import os, re, pprint
from termcolor import colored


class CypressTestFile:
    def __init__(self, name, cypress_file_path, remote_images_path, local_images_path, repository_url, htmlpreview):
        self.name = name
        self.cypress_file_path = cypress_file_path
        self.remote_images_path = remote_images_path
        self.local_images_path = local_images_path
        self.repository_url = repository_url
        self.htmlpreview = htmlpreview
        file = open(cypress_file_path, "r")
        self.text = file.read()
        file.close()

    def _delete_screenshots(self):
        for image_path in os.scandir(self.local_images_path):
            os.remove(image_path)

    def document(self, mode):
        doc = self.text
        for repl in self._replacements(): # Recurse
            # FIXME: Filter
            # mode = python or html
            doc = re.sub(repl[0], repl[1][mode], doc, flags=re.M)
        return "<table>" + doc + "</table>"

    def _header(self):
        return f"""
        <img src="https://mwstake.org/mwstake/branding/logo.png" style="width:50px;"/>
        <ol>
            <li>
                This is the <b>documentation on the use cases</b> enabled by <a href="{self.repository_url}">{self.repository_url}</a>.
            </li>
            <li>
                These use cases based on <a href='{self.repository_url}/tree/main/cypress/e2e/CRUD/{self.file_name()}'>{self.file_name()}</a> are curated by MWStake and currently <b>certified for MWCore 1.36</b> in conjunction with <a href="">this set of extensions</a>.
            </li>
        </ol>
        """

    def file_name(self):
        return self.cypress_file_path.name.split('/')[-1]

    def _script(self):
        return """
            <script>
            </script>
        """

    def save_html_document(self, html_file_path):
        html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>{self.name}</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                {self._script()} 
                {self._header()}
                {self.document("html")}
            </body>
            </html>
            
        """
        file = open(html_file_path, "w")
        file.write(html + CypressTestFile.styles())
        file.close()

    @staticmethod
    def styles():
        return """
            <style>
                td {
                    border: 1px solid gray;
                }
                .hide {
                    display: none;
                }
                body {
                    font-family:Sans-serif;
                    line-height:150%;
                    padding:50px;
                }                
                .describe {
                    padding-top:10px;
                    
                }
                .aspect {
                    font-weight:bold; color:green;text-decoration: underline;
                }
                .feature {
                    font-weight:bold; 
                    color:green;padding-bottom:5px; 
                }
                .goto {
                    font-weight:bold; color:orange;
                }
                .do {
                    font-weight:bold; color:orange;
                }
                .left20 {
                    padding-left:20px; padding-top:20px;  
                }
                .left40 {
                    padding-left:40px; padding-top:5px; 
                }
                .left60 {
                    padding-left:60px; padding-top:5px; 
                }
                .comment {
                    color:grey;
                }
                .screenshot {
                    color:green;
                }
                a {
                    text-decoration:none;
                }
                td {
                    vertical-align:top;
                    padding:10px;
                }
                .screenshotPNG {
                    box-shadow: -5px -5px 5px grey;
                    width:500px;
                }
                .command {
                    font-weight:bold;
                }
                .arguments {
                    font-family:mono;
                }
            </style>
        """

    def _screenshot_name_patterns(self):
        html = """
                    <tr><td>
                        <div class='left40'>\\1</div></td><td>
                        <div class='left60'>
                            <img class="screenshotPNG" src='"""+self.remote_images_path+"""/\\1.png' />
                        </div>
                    </td></tr>"""
        return [
            [
                r"cy.__take_screenshot\(\"(.*)\"\);",
                {
                    "python": colored("See", "blue") + " \\1",
                    "html": html,
                    "image": "\\1",
                }
            ],
            [
                r"cy.clip_screenshot_and_click\(\n?\$target,[\n ]?\"(.*)\"\n?\);",
                {
                    "python": colored("See", "blue") + " \\1",
                    "html": html,
                    "image": "\\1",
                }
            ],
            [
                r"cy.clip_screenshot_and_save_search_facet\(\n?unixTimestamp,[\n ]?\"(.*)\"\n?\);",
                {
                    "python": colored("See", "blue") + " \\1",
                    "html": html,
                    "image": "\\1",
                }
            ]
        ]

    
    def _replacements(self):
        return [
            [r"^ *(cy.(get)).+", {"python": "", "html": ""}],
            [r"^(?! *(describe|it|cy.|//)).+\n", {"python": "", "html": ""}],
            [
                r"^describe\(\"([\w -:]*)\",.*",
                {
                    "python": colored("ASPECT", "green", attrs=["bold", "underline"]) + " \\1\n",
                    "html": "<tr><td colspan=2><div class='describe'><span class='aspect'>Aspect</span>: <b>\\1</b></div></td></tr>",
                },
            ],
            [
                r"^ ?it\.?[a-z]*\(\"(.*)\"",
                {
                    "python": colored("Use Case: ", "green", attrs=["bold"]) + "it \\1",
                    "html": "<tr><td colspan=2><div class='left20'><span class='feature'>Use Case</span>: <b>it \\1</b></div></td></tr>",
                },
            ],
            [
                r"cy.visit\(\"(.*)\"\);",
                {
                    "python": colored("Go to", "yellow") + " \\1",
                    "html": "<tr><td colspan=2><div class='left40'><span class='goto'>Go to</span> \\1</div></td></tr>",
                },
            ]
        ] + self._screenshot_name_patterns() + [
            [   # Remove cy.__* commands
                r"cy.(__\w*)\(.*(\);)?",
                {
                    "python": "",
                    "html": "",
                },
            ],
            [
                r"cy.(\w*)\(.*(\);)?",
                {
                    "python": colored("Do", "yellow") + " \\1()",
                    "html": f"<tr><td colspan=2><div class='left40'><span class='do'>Do</span> <a href='{self.htmlpreview}/commands.html' class='command' title='Click to get an explanation for \\1'>\\1</a>(<span class='arguments'></span>)</div></td></tr>",
                },
            ],
            [   
                r", \((.*)\) => {",
                {
                    "python": "\\1",
                    "html": "\\1"
                }
            ],
            [   r"\);\n",
                {
                    "python": "",
                    "html": ""
                }
            ],
            [
                r"^( +)// *(.*)$",
                {
                    "python": colored("\\1\\2", "yellow"),
                    "html": "<tr><td colspan=2><div class='left40 comment'>\\1\\2</div></td></tr>",
                },
            ],
        ]

    @staticmethod
    def list_commands(commands_file_path, html_file_path):
        file = open(commands_file_path, "r")
        text = file.read()
        file.close()
        commands_list = "<hr/>".join(
            list(
                map(
                    lambda x: f"<span class='command'>{x[0]}</span>(<span class='arguments'>{x[1]}</span>)",
                    re.findall(r"Cypress\.Commands\.add\(\"(\w+)\", \(([, \w]*)\) => {", text),
                )
            )
        )
        html = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>MWStake Doc</title>
                <link rel="stylesheet" href="style.css">
            </head>
            <body>
                <script src="index.js"></script>
                {commands_list}
                {CypressTestFile.styles()}
            </body>
            </html>
            
        """
        file = open(html_file_path, "w")
        file.write(html)
        file.close()
        return
