import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingstion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # reading the data from mysql
            df = read_sql_data()
            logging.info("Reading completed MySQL Database")
            os.makedirs(
                os.path.dirname(self.ingstion_config.train_data_path), exist_ok=True
            )
            df.to_csv(self.ingstion_config.raw_data_path, index=False, header=True)

            train_set, test_stt = train_test_split(df, test_size=0.2, random_state=42)
            df.to_csv(self.ingstion_config.train_data_path, index=False, header=True)
            df.to_csv(self.ingstion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")

            return (
                self.ingstion_config.train_data_path,
                self.ingstion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
