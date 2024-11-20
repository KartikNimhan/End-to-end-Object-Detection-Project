import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constants start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

# Google Drive URL for unzipped data
DATA_DOWNLOAD_URL: str = (
    "https://drive.google.com/drive/folders/1jyds1XqDip9CJtT0ltXeKsm0j5GK9ir5?usp=sharing"
)

"""
Data Validation related constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "status.txt"
DATA_VALIDATION_REQUIRED_FILES = ["input_videos", "processed_landmarks"]

"""
Model Trainer related constants start with MODEL_TRAINER VAR NAME
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

# Path to the trained pickle model file
MODEL_TRAINER_PICKLE_FILE: str = (
    "D:/End to end machine learning projects/Object Detection Project/End-to-end-Object-Detection-Project/signLanguage/Notebooks/model.p"  # Replace with the correct path to your pickle file
)

MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16

"""
Model Pusher related constants start with MODEL_PUSHER VAR NAME
"""
BUCKET_NAME = "sign-lang-2024"  # Bucket name for S3 or any other storage service
S3_MODEL_NAME = (
    "best.pt"  # Update if needed; otherwise, you can remove this if not applicable
)
