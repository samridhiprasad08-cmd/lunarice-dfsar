from src.core.pipeline import Pipeline

from src.modules.m01_data_ingestion import DataIngestion
from src.modules.m02_preprocessing import RadiometricPreprocessing
from src.modules.m03_shadow_detection import PermanentShadowAnalysis


def main():
    pipeline = Pipeline()

    pipeline.add_module(DataIngestion())
    pipeline.add_module(RadiometricPreprocessing())
    pipeline.add_module(PermanentShadowAnalysis())

    pipeline.run()


if __name__ == "__main__":
    main()