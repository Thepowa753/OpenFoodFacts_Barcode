import setuptools

setuptools.setup(
    name = "OpenFood",
    version = "0.0.2",
    author = "Fede.Breg",
    author_email = "author@example.com",
    description = "Query openFood to get data from barcode",
    long_description = "Query openFood to get data from barcode",
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "OpenFood"},
    packages = setuptools.find_packages(where="OpenFood"),
    python_requires = ">=3.6"
)