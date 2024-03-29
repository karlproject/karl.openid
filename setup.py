__version__ = '0.1dev'

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

REQUIRES = ['setuptools', 'karl']

setup(name='karl.openid2',
      version=__version__,
      description='OpenID 2.0 integration for KARL',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        ],
      keywords='web wsgi karl',
      author="Open Society Institute",
      author_email="osi-dev@lists.palladion.com",
      url="http://launchpad.net/~teamkarl",
      license="GPL",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['karl'],
      zip_safe=False,
      #tests_require = require,
      install_requires = REQUIRES,
      test_suite="nose.collector",
      #entry_points = """\
      #[console_scripts]
      #remove_old_tickets = karl.openid2.scripts.karl_openid_2xxx
      #"""
)
