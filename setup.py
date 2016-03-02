#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='menoo',
      version='0.0.2',
      description='a simple, deploy ready interactive cli menu',
      author='Roy Sommer',
      url='https://www.github.com/illberoy/menoo',
      download_url='https://github.com/illberoy/menoo/tarball/0.0.2',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['menoo'],
      install_requires=['readchar==0.7.0', 'blessings==1.6.0'])
