from setuptools import setup, find_packages

setup(
    name='upath',
    version='1.0',
    author='Igor Kalat',
    author_emain='igor.kalat@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        upath=upath.upath:cli
    ''',
)
