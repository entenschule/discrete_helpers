from setuptools import find_packages, setup


setup(

   name='discretehelpers',
   version='0.0.1',
   description='library for discrete mathematics (playground version)',
   author='Watchduck',
   author_email='no@example.com',
   license='MIT',

   packages=find_packages(),
   install_requires=['numpy', 'networkx']

)
