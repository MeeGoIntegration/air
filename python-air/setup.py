from distutils.core import setup
from setuptools import setup

setup(name='python-air',
      version='1.0',
      description='Python air module',
      author='David Greaves',
      author_email='david@dgreaves.com',
      url='http://github.com/lbt/ruote-amqp-pyclient',
      packages=['AIR',],
      requires=['amqplib', 'json']
     )
