# tests-documentation-maker (TDM)

* "https://raw.githubusercontent.com/dataspects/DataspectsSearch/main/readme_images"
* "/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/readme_images"

```
repository_url="https://github.com/dataspects/DataspectsSearch" \
cypress_test_folder="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/e2e" \
htmlpreview="https://htmlpreview.github.io/?https://github.com/dataspects/DataspectsSearch/blob/main/" \
images_path="https://raw.githubusercontent.com/dataspects/DataspectsSearch/main/readme_images" \
tests_doc_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/doc.html" \
commands="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/cypress/support/commands.js" \
commands_html="/home/lex/mwstakeorgdevclone/extensions/DataspectsSearch/commands.html" \
python3 -m unittest test_parse_cypress_tests.py
```