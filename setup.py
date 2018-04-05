from setuptools import setup, find_packages

setup(
    name='pynopla',
    version='0.0.1',
    author='Marius Räsener',
    author_email='m.raesener@gmail.com',
    description='A simple python api for the Inopla Cloud PBX (inopla.de)',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'aiohttp'
    ]
)
