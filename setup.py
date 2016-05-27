from setuptools import setup

VERSION = '1.0'

setup(
    name = 'cloudpayments',
    packages = ['cloudpayments'],

    description = 'CloudPayments Python Client Library',
    long_description = open('README.rst').read(),

    version = VERSION,

    author = 'Antida software',
    author_email = 'info@antidasoftware',
    license = 'MIT license',

    url = 'https://github.com/antidasoftware/cloudpayments-python-client',
    download_url = 'https://github.com/antidasoftware/cloudpayments-python-client/tarball/%s' % VERSION,

    requires = [
        'requests (>=2.9.1)',
        'pytz (>=2015.7)'
    ],

    install_requires = [
        'requests >=2.9.1',
        'pytz >=2015.7'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)