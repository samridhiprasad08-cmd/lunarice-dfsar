"""
=========================================================
MODULE 1

Data Ingestion

Author:
Team ___________

=========================================================
"""

from src.core.base_module import BaseModule
from src.utils.logger import logger


class DataIngestion(BaseModule):

    def __init__(self):

        super().__init__("Module 01 : Data Ingestion")

    def validate_input(self):

        logger.info("Checking required datasets...")

    def process(self):

        logger.info("Loading DFSAR data...")

    def validate_output(self):

        logger.info("Checking loaded datasets...")

    def save_results(self):

        logger.info("Module 1 completed.")