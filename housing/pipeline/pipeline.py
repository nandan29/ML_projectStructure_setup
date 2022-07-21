from housing.component.data_ingestion import DataIngestion
from housing.config.configuration import Configuration
from housing .logger import logging
from housing.exception import housing_exception
import os, sys

from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.component.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self, config:Configuration = Configuration())->None:
        self.config = config




    def start_data_ingestion(self):
        try:
            data_ingestion_configuration  = self.config.get_data_ingestion_config() #getting data ingestion config
            #creating an object for DataIngestion and feeding into DataIngestionConfig as an i/p, generated from configuaration file.
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_configuration)

            #now we will trigger the data ingestion pipeline
            data_ingestion.initiate_DataIngestion()
        except Exception as e:
            raise housing_exception(e,sys) from e