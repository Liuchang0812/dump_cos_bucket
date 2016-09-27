from distutils.core import setup
from setuptools import find_packages

setup(
    name='cos_dumps_file_list',
    version='0.0.2',
    packages=['dump_bucket'],
    url='https://www.qcloud.com/',
    license='MIT',
    author='liuchang',
    author_email='liuchang0812@gmail.com',
    description='simple tool that could be used to dump file list within cos bucket',
    entry_points={
        'console_scripts': [
            'cos_dumps = dump_bucket.main:_main'
        ]
    },
    install_requires=[
        'qcloud-cos',
        'requests'
    ],
    package=find_packages(),
)
