# tests-documentation-maker (TDM)

```bash
cd /home/lex/cypress/Cypress && ./Cypress
```

```bash
git clone https://github.com/dataspects/tests-documentation-maker.git
cd tests-documentation-maker
```

```bash
name="Doc for dataspects Search" \
repository_url="https://github.com/dataspects/DataspectsSearch" \
cypress_test_folder="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/e2e" \
htmlpreview="https://htmlpreview.github.io/?https://github.com/dataspects/DataspectsSearch/blob/master/" \
remote_images_path="https://raw.githubusercontent.com/dataspects/DataspectsSearch/master/readme_images" \
local_images_path="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/readme_images" \
tests_doc_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/doc.html" \
commands="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/support/commands.js" \
commands_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/commands.html" \
python3 -m unittest test_parse_cypress_tests.py
```

View `tests_doc_html` in a browser.
