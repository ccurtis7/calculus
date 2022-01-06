from setuptools import setup, find_packages
from calculus.calculus import __version__

setup(
    name='calculus',
    version='0.0.1',

    url='https://github.com/ccurtis7/calculus',
    author='Chad Curtis',
    author_email='chad.curtis@nsc.edu',
    install_requires=['numpy>=1.19.2'],
    py_modules=find_packages()
)
