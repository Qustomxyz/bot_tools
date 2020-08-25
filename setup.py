import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="package_template",
    version="0.0.1",
    author="Qustomxyz",
    author_email="qbus.klb@gmail.com",
    description="Template package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Qustomxyz/package_template",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
