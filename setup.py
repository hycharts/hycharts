import os

from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='hycharts',
    version='0.1.0',
    description='HyCharts',
    long_description=(read('README.md')),
    url='http://github.com/hycharts/hycharts/',
    license='MIT',
    author='Edwin Hu, Mac Gaulin',
    author_email='eddyhu@gmail.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
