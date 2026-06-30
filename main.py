from src.core.pipeline import Pipeline
from src.modules.m01_data_ingestion import DataIngestion
from src.modules.m02_preprocessing import RadiometricPreprocessing


def main():
    pipeline = Pipeline()
    pipeline.add_module(DataIngestion())
    pipeline.add_module(RadiometricPreprocessing())
    pipeline.run()


if __name__ == "__main__":
    main()