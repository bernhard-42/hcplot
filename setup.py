import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hcplot",
    version="0.3.0",
    author="Bernhard Walter",
    author_email="bwalter@gmail.com",
    description=("ggplot with highcharts iun a python'ish way"),
    license="Apache License 2.0",
    keywords="jupyter ipython highcharts visualizations",
    packages=find_packages(),
    package_data={'hcplot': ['js/*', 'css/*']},
    long_description=read('Readme.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python'",
        "Programming Language :: Python :: 2'",
        "Programming Language :: Python :: 3'"
    ]
)
