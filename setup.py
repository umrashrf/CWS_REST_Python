#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='nabcommerce',
    version='1.0.0',
    url='https://nabvelocity.com/',
    description='Python wrapper for NABVelocity\'s REST API',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    zip_safe=False,
    install_requires=[
        'six',
    ],
)
