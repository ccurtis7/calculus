from setuptools import setup, find_packages
from calculus.calculus import __version__

setup(
    name='calculus',
    version=__version__,

    url='https://github.com/ccurtis7/calculus',
    author='Chad Curtis',
    author_email='chad.curtis@nsc.edu',

    py_modules=find_packages()
)
