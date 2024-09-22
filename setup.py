#### it helps in puttimg package in pip setup.py is a Python script that serves as the build script for setuptools. Setuptools is a Python tool that automates the 
##packaging process and works in coordination with pip to distribute packages.

from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[req.replace("\n","") for req in reqirements] ## removing \n or line and comboning
    return reqirements

setup(
    name='daimond rate predicition',
    version = '0.0.1',
    author = 'adharsh',
    author_email = 'adharshsobhanan@gmail.com',
    install_requires = get_requirements('requirement.txt'),
    packages=find_packages())
