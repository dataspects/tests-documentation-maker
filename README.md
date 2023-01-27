# tests-documentation-maker (TDM)

```bash
cd /home/lex/cypress/Cypress && ./Cypress
```

```bash
git clone https://github.com/dataspects/tests-documentation-maker.git
cd tests-documentation-maker
```

```bash
name="Doc for MediaWiki Extension:Dataspects" \
repository_url="https://github.com/dataspects/Dataspects" \
cypress_test_folder="/home/lex/mwstakeorgdevclone/extensions/Dataspects/cypress/e2e" \
htmlpreview="https://htmlpreview.github.io/?https://github.com/dataspects/Dataspects/blob/master/" \
remote_images_path="https://raw.githubusercontent.com/dataspects/Dataspects/master/readme_images" \
local_images_path="/home/lex/mwstakeorgdevclone/extensions/Dataspects/readme_images" \
doc_folder_path="/home/lex/mwstakeorgdevclone/extensions/Dataspects/doc.html" \
commands="/home/lex/mwstakeorgdevclone/extensions/Dataspects/cypress/support/commands.js" \
commands_html="/home/lex/mwstakeorgdevclone/extensions/Dataspects/commands.html" \
python3 -m unittest test_parse_cypress_tests.py
```

View `doc_folder_path` in a browser.
