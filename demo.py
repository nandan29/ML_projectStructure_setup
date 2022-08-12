from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.config.configuration import Configuartion
import os,sys
from housing.logger import logging

def main():
    try:
        config_file_path = os.path.join("config","config.yaml")

        pipeline = Pipeline(Configuartion(config_file_path=config_file_path))
        pipeline.run_pipeline()
        
    except Exception as e:
        raise HousingException(e,sys)



if __name__ == '__main__':
    main()