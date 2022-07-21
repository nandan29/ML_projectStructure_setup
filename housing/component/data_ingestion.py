from curses import raw
import sys
from tkinter import E
from turtle import down
from housing.entity.config_entity import DataIngestionConfig
from housing.exception import housing_exception
from housing.logger import logging
import os
from housing.entity.artifact_entity import  DataIngestionArtifact

import tarfile
from six.moves import urllib

import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

"""
here for each named tuple element in DataIngestionArtifact , we will define a function to get the o/p

I/P to these function will be elements of named tuple in DataIngestionConfig




"""
class DataIngestion:

    def __init__(self,data_ingestion_config : DataIngestionConfig):
        try:
            logging.info("Data Ingestion log started")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise housing_exception(e,sys) from e
    

    def download_housing_data(self):
        try:
            download_url=self.data_ingestion_config.dataset_download_url

            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            os.makedirs(tgz_download_dir,exist_ok=True)

            housing_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)

            logging.info(f"downloading file from {download_url}")
            urllib.request.urlretrieve(download_url,tgz_file_path)

            logging.info("file download completed successfully :{tgz_file_path}")
            return tgz_file_path
        except Exception as e:
            raise housing_exception(e,sys) from e


    def extract_tgz_file(self,tgz_file_path):

        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedir(raw_data_dir)

            logging.info("extracting tgz file : {tgz_file_path} at location {raw_data_dir}")
            f= tarfile.open(tgz_file_path)
            f.extractall(path=raw_data_dir)
            logging.info("extraction completed and file is successfully stored in {raw_data_dir}")

        except Exception as e:
            raise housing_exception(e,sys) from e


    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            housing_file_path = os.path.join(raw_data_dir,file_name)

            logging.info("read the csv file")
            housing_data_frame = pd.read_csv(housing_file_path)

            housing_data_frame["income_cat"] = pd.cut(
                    housing_data_frame["median_income"],
                    bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
                    labels=[1,2,3,4,5]
                )
                

            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index,test_index in sss.split(housing_data_frame, housing_data_frame["income_cat"]):

                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"],axis=1)
                strat_test_set = housing_data_frame.loc[test_index].drop(["income_cat"],axis=1)


            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                                        file_name)
            
            test_file_path= os.path.join(self.data_ingestion_config.ingested_test_dir,
                                                                        file_name)


            ingested_train_dir = os.makedirs(self.data_ingestion_config.ingested_train_dir)
            ingested_test_dir = os.makedirs(self.data_ingestion_config.ingested_test_dir)

            if strat_train_set is not None:
                logging.info("extracting training dataset to the filepath :{train_file_path}")
                strat_train_set.to_csv(train_file_path,index=False)


            if strat_test_set is not None:
                logging.info("extarcting test dataet to the path : {test_file_path}")
                strat_test_set.to_csv(test_file_path,index=False)


            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
            test_file_path=test_file_path,is_ingested=True,message = "Data Ingestion completed successfully")

            logging.info("DataIngestionArtifact: {DataIngestionArtifact}")

            return DataIngestionArtifact
        
        except Exception as e:
            raise housing_exception(e,sys) from e


    def initiate_DataIngestion(self)->DataIngestionArtifact:
        try:
            download_tgz_file_path = self.download_housing_data()
            self.extract_tgz_file(download_tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:

            raise housing_exception(e,sys) from e

    def __del__(self):
        logging.info("data ingestion log completed")
