#!/usr/bin/env python

from setuptools import setup

setup(name='tap-prometheus',
      version='0.0.2',
      description='Singer.io tap for extracting data from the Prometheus API',
      author='JustEdro',
      url='https://github.com/JustEdro',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_prometheus'],
      install_requires=[
          'singer-python==5.2.3',
          'promalyze==0.0.2',
          'pytz'
      ],
      dependency_links=[
          'git+https://github.com/miroapp/promalyze.git',
      ],
      entry_points='''
          [console_scripts]
          tap-prometheus=tap_prometheus:main
      ''',
      packages=['tap_prometheus'],
      package_data={
          'tap_prometheus/schemas': [
              'agents.json'
          ],
      },
      include_package_data=True,
      )
