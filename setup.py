# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="data-quality-tests",
    version="3.1.1",
    description="Data Quality Check Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beekiran00/Data-Quality",
    author="Bhanu Venkata Kiran Velpula",
    author_email="beekiran00@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["data_quality_tests"],
    include_package_data=True,
    install_requires=["pandas","numpy"]
)