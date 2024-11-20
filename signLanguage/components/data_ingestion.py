import os
import sys
from six.moves import urllib
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SignException(e, sys)

    def download_data(self) -> str:
        """
        Fetch data from the given URL (uncompressed).
        """
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            data_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(data_download_dir, exist_ok=True)
            data_file_name = os.path.basename(dataset_url)
            data_file_path = os.path.join(data_download_dir, data_file_name)

            logging.info(f"Downloading data from {dataset_url} into file {data_file_path}")
            urllib.request.urlretrieve(dataset_url, data_file_path)
            logging.info(f"Downloaded data from {dataset_url} into file {data_file_path}")

            return data_file_path

        except Exception as e:
            raise SignException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process.
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            data_file_path = self.download_data()

            data_ingestion_artifact = DataIngestionArtifact(
                data_file_path=data_file_path,
                feature_store_path=self.data_ingestion_config.feature_store_file_path,
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise SignException(e, sys)
