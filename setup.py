from setuptools import find_packages, setup
from typing import List




PROJECT_NAME ="HOUSING PRICE PREDICTION"
VERSION="0.0.1"
AUTHOR="SHUBHAM SRIVASTAVA"
DESCRIPTION="Setting up the entire ML pipeline"
REQUIREMENTS_FILE_NAME = "requirements.txt"




def get_requirements_list()->List[str]:
    """
    this function is going to return a list of requirements as strings , present in requirements.txt file

    here we are removing -e .  , as we know that find_packages() is equivalent to -e . and find_packages() will install
    our custom package llly -e . will install our custom packages so removing it in order to avoid installing our
    custom package 2 times.

    
    """
    f=open(REQUIREMENTS_FILE_NAME,"r")
    requirement_list=f.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list].remove("-e .")
    return requirement_list

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),   #IMPORTANT
install_requires=get_requirements_list() #IMPRORTANT
)
