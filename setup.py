from setuptools import setup

NAME = 'aem-client'
PACKAGE_NAME = 'aemclient'


def readme():
    with open('README.md') as f:
        return f.read()


setup(name=NAME,
      version='1.0',
      description='',
      long_description=readme(),
      classifiers=[
        'Development Status :: Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6.5',
      ],
      keywords='',
      url='',
      author='Steve William, Arbor Networks, Inc.',
      author_email='steve.william@netscout.com',
      license='MIT',
      packages=[PACKAGE_NAME],
      install_requires=[
          'requests',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
