"""
Main entry point.

Lunar Ice Detection Framework
"""

from src.core.pipeline import Pipeline

from src.modules.m01_data_ingestion import DataIngestion


def main():

    pipeline = Pipeline()

    pipeline.add_module(DataIngestion())

    pipeline.run()


if __name__ == "__main__":

    main()