# from distutils.core import setup
from setuptools import setup

setup(
  name = 'newscraper',
  packages = ['newscraper'], # this must be the same as the name above
  install_requires=['beautifulsoup4==4.4.1',
                   'cffi==1.4.1',
                   'cryptography==41.0.4',
                   'enum34==1.1.1',
                   'gevent==1.0.2',
                   'greenlet==0.4.9',
                   'idna==2.0',
                   'ipaddress==1.0.15',
                   'lxml==4.9.1',
                   'ndg-httpsclient==0.4.0',
                   'pyasn1==0.1.9',
                   'pycparser==2.14',
                   'pyOpenSSL==0.15.1',
                   'requests==2.20.0',
                   'six==1.10.0'],
  scripts=['bin/newscrape'],
  license='GNU GPL v2',
  version = '0.2',
  description = 'Scrapes Indian news sites for news related to keywords',
  author = 'thekindlyone',
  author_email = 'dodo.dodder@gmail.com',
  url = 'https://github.com/thekindlyone/newscraper', # use the URL to the github repo
  download_url = 'https://github.com/thekindlyone/newscraper/tarball/0.2', # I'll explain this in a second
  keywords = ['indian', 'news', 'scraping'], # arbitrary keywords
  classifiers = [],
)