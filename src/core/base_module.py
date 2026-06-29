"""
=========================================================
Base Module

Every scientific module in the Lunar Ice Detection
Framework inherits from this class.

Author:
Team ________

=========================================================
"""

from abc import ABC, abstractmethod
from pathlib import Path

from src.utils.logger import logger


class BaseModule(ABC):
    """
    Base class for every module.
    """

    def __init__(self, module_name: str):

        self.module_name = module_name

        logger.info(f"{module_name} initialized.")

    def run(self):

        logger.info(f"Running {self.module_name}")

        self.validate_input()

        self.process()

        self.validate_output()

        self.save_results()

        logger.info(f"{self.module_name} completed successfully.")

    @abstractmethod
    def validate_input(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def validate_output(self):
        pass

    @abstractmethod
    def save_results(self):
        pass