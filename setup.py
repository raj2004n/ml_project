from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    Return the list of requirements from the requirements file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        # if -e . is present, then replace it with .
        if '-e .' in requirements:
            requirements.remove('-e .')
            requirements.append('.')

setup(
    name='ml_project',
    version='0.1',
    author='Raj Negi',
    author_email='raj2004n@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )