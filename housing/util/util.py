
from housing.exception import HousingException
import yaml
import sys


def read_yaml_file(file_path:str)->dict:

    try:
        yaml_file=open(file_path,"r")

        config_info = yaml.safe_load(yaml_file)
        return config_info
    except Exception as e:
        raise HousingException(e,sys) from e

