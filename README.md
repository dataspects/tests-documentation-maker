# tests-documentation-maker (TDM)

* "https://raw.githubusercontent.com/dataspects/DataspectsSearch/main/readme_images"
* "/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/readme_images"

```bash
name="Doc for dataspects Search" \
repository_url="https://github.com/dataspects/DataspectsSearch" \
cypress_test_folder="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/e2e" \
htmlpreview="https://htmlpreview.github.io/?https://github.com/dataspects/DataspectsSearch/blob/main/" \
remote_images_path="https://raw.githubusercontent.com/dataspects/DataspectsSearch/main/readme_images" \
local_images_path="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/readme_images" \
tests_doc_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/doc.html" \
commands="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/support/commands.js" \
commands_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/commands.html" \
python3 -m unittest test_parse_cypress_tests.py
```