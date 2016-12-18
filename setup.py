#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thanks to Kenneth Reitz, I stole the template for this

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

PYTHON3 = sys.version_info[0] > 2

required = ['requests>=2.9', 'websocket-client==0.35.0',
        'beautifulsoup4==4.4.1', 'html5lib==0.9999999', 'pyfiglet==0.7.4',
        'certifi==2015.04.28']
if not PYTHON3:
    required += ['importlib>=1.0.3']

packages = ['limbo', 'limbo.plugins']

try:
    longdesc = open("README.rst").read()
except:
    longdesc = ''

setup(
    name='limbo',
    version='5.0.3',
    description='Simple and Clean Slack Chatbot',
    long_description=longdesc,
    author='Bill Mill',
    author_email='bill@billmill.org',
    url='https://github.com/llimllib/limbo',
    packages=packages,
    scripts = ['bin/limbo'],
    package_data={'': ['LICENSE',], '': ['limbo/plugins/*.py']},
    include_package_data=True,
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ),
)
