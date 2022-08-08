from housing.component.data_ingestion import DataIngestion
from housing.config.configuration import  Configuartion
from housing .logger import logging
from housing.exception import HousingException
import os, sys

from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.component.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self, config:Configuartion)->None:
        self.config = config


    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config= self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e






    def run_pipeline(self):
        try:
            #data ingestion
            data_ingestion_Artifact = self.start_data_ingestion()

            return data_ingestion_Artifact
        except Exception as e:
            raise HousingException(e,sys) from e