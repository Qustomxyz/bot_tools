# package_template
Template repository

You should replace this information in setup.py:

for my project:
- name="package_template",
- description="Template package",
- url="https://github.com/Qustomxyz/package_template",

for any other projects:
Make some replace as you wish. Good candidates:
- and all above
- author
- author_email
- url

Yes, you should replace "README.md" too. Read and burn it :)

## How to make package?
Make sure you have the latest versions of setuptools and wheel installed:
`python3 -m pip install --user --upgrade setuptools wheel`

then make this command:
`python3 setup.py sdist bdist_wheel`

for more details see this tutorial:
[How to load my package into Pypi](https://packaging.python.org/tutorials/packaging-projects/)
