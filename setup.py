from setuptools import setup

NAME = 'edm-client'
PACKAGE_NAME = 'edmclient'


def readme():
    with open('README.md') as f:
        return f.read()


setup(name=NAME,
      version='1.0',
      description='Edge Defense Manager Client',
      long_description=readme(),
      classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      keywords='',
      url='',
      author='Steve William, NETSCOUT Systems, Inc.',
      author_email='swilliam@netscout.com',
      license='MIT',
      packages=[PACKAGE_NAME],
      install_requires=[
          'requests',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
