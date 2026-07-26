from setuptools import setup, find_packages

setup(
    name='simplecolorlogger', 
    version='0.1', 
    packages=find_packages(), 
    install_requires=[
        'colorama>=0.4.6'
    ],
)
