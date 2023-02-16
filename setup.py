from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Bayesian Network creation'

# Setting up
setup(
    name="NetBayesian",
    version=VERSION,
    author="Jun Woo Lee",
    author_email="<juunshuu00@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'bayesian network', 'bayesian', 'network'],
)