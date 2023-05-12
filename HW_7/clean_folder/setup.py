from setuptools import setup, find_namespace_packages

setup(
    name='Clean folder',
    version='1.0.0',
    description='sorts folder',
    author='Ivan Ralitniy',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.clean:main'
        ]
    }
)