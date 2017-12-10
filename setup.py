import os
import re

from setuptools import find_packages, setup


def get_version(package):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        package, '__init__.py')
    with open(path, 'r') as file:
        source = file.read()
    m = re.search(r'__version__ = ["\'](.+)["\']', source)
    if m:
        return m.group(1)
    else:
        return '0.0.0'


setup(
    name='iroha',
    version=get_version('iroha'),
    description='Python Packaging Tutorial',
    url='https://github.com/daizutabi/iroha',
    author='daizutabi',
    author_email='daizutabi@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    install_requires=['click'],
    entry_points={
        'console_scripts': [
           'iroha = iroha.main:cli',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
