from distutils.core import setup
setup(
  name = 'newscraper',
  packages = ['newscraper'], # this must be the same as the name above
  install_requires=[
      'beautifulsoup4',
      'lxml',
      'requests'   ],
  version = '0.1',
  description = 'A random test lib',
  author = 'Peter Downs',
  author_email = 'peterldowns@gmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)