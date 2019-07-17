from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='webassembly',
    version='0.0.1',
    description='WebAssembly Python standard API prototype',
    long_description=readme,
    author='Ivan Enderlin',
    author_email='ivan.enderlin@hoa-project.net',
    url='https://github.com/Hywan/wasm-python-api',
    packages=find_packages(exclude=('tests', 'docs'))
)
