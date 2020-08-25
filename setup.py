import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="bot_tools",
    version="0.0.1",
    author="Qustomxyz",
    author_email="qbus.klb@gmail.com",
    description="Small scripts collection for telegram bot dev",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Qustomxyz/bot_tools",
    packages=['requests', 'python-dotenv'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
