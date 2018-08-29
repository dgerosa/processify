#python setup.py sdist upload -r test
#python setup.py sdist upload

from setuptools import setup

setup(
    name='processify',
    #version='0.1',
    url='https://gist.github.com/schlamar/2311116',
    include_package_data=True,
    zip_safe=False,
)
