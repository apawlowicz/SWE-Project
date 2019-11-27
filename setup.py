import os
from setuptools import setup, find_packages

setup(name='Data Analytics Tool',
      version='1.0',
      description='Software engineering project for The Hartford',
      author='Will Fraher, Aleks Pawlowicz, Georgios Savvidis, Kelbin Rodriguez',
      packages=find_packages('analysis'),
      scripts=['analysis/frequencies.py','analysis/clustering.py','analysis/correlation_matrix.py']
     )
