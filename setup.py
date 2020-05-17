from setuptools import setup, find_packages

setup(
    name='scrap',
    version='0.1.0',
    author='Yuval Helman',
    description='A module for Oreily\'s Web scraping with Python book',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest', 'pytest-cov'],
)

