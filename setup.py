from setuptools import setup, find_packages

setup(
    name="hexlet-code",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pyyaml>=6.0"],
    entry_points={
        'console_scripts': [
            'gendiff=hexlet_code.scripts.gendiff:main',
        ],
    },
)
