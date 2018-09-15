# Uploading package to PyPi.

from setuptools import setup

setup(name='schoologypy',
      version='0.2.0',
      description='A Python wrapper for Schoology\'s API.',
      url='https://github.com/ErikBoesen/schoologypy',
      author='Erik Boesen',
      author_email='me@erikboesen.com',
      license='MIT',
      packages=['schoologypy'],
      install_requires=['requests', 'requests-oauthlib', 'oauthlib'],
      zip_safe=False)
