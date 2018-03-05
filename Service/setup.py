from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

__version__ = "0.0.1"

setup(
    author='Jeff Wang',
    author_email='jeffwji@test.com',

    version_command='git describe --always --long --dirty=-dev',

    name = "service",
    packages = find_packages(
        exclude=['tests', '*.tests', '*.tests.*']
    ),

    package_data = {
        '':[ 'config/*.properties', '*.md', 'requirements.txt' ],
    },

    install_requires=requirements,
)
