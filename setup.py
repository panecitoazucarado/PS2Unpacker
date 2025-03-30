from setuptools import setup, find_packages

setup(
    name='PS2Unpacker',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'python-dateutil'
    ],
)