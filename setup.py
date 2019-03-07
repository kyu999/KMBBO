#!/usr/bin/env python

from setuptools import find_packages, setup


description = 'Efficient and Scalable Batch Bayesian Optimization Using K-Means'
REQUIRED_PACKAGES = [
    'GPy==1.9.6'
]

setup(name='kmbbo',
      version='0.0.1',
      license='MIT',
      description=description,
      long_description=description,
      author="kyu999",
      author_email="kyukokkyou999@gmail.com",
      maintainer="kyu999",
      maintainer_email="kyukokkyou999@gmail.com",
      url='https://github.com/kyu999/KMBBO',
      packages=find_packages(),
      install_requires=REQUIRED_PACKAGES,
)
