#!/usr/bin/env python
from distutils.core import setup

description = 'Simple and powerful mocking framework with '\
              'extensible assertion matchers'

setup(name='pungi',
      version='0.1.3',
      description=description,
      long_description=description,
      author='Deepak N',
      author_email='endeep123@gmail.com',
      maintainer='Deepak N',
      maintainer_email='endeep123@gmail.com',
      url='https://github.com/endeepak/pungi',
      packages=['pungi'],
      license='MIT',
      classifiers=[
                    'Programming Language :: Python',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: OS Independent',
                    'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Topic :: Software Development :: Testing'
                    ]
     )
