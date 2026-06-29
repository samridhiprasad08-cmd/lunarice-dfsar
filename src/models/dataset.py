"""
===========================================================
DFSAR DATASET MODEL
===========================================================

Project:
Lunar Ice Detection and Characterization System
using Chandrayaan-2 DFSAR

Description:
This file defines the master dataset object used throughout
the complete processing pipeline.

Every module receives and returns this object.

Author:
Team SAR
===========================================================
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class DFSARDataset:
    """
    Master scientific dataset object.

    Stores all metadata, radar information,
    geometry information and processing status
    required throughout the complete pipeline.
    """

    # ======================================================
    # Mission Information
    # ======================================================

    mission: str = ""
    instrument: str = ""
    product_type: str = ""

    # ======================================================
    # Radar Information
    # ======================================================

    frequency_band: str = ""
    polarization: str = ""

    orbit_number: Optional[int] = None

    acquisition_time: str = ""

    # ======================================================
    # Observation Geometry
    # ======================================================

    incidence_angle: Optional[float] = None

    look_direction: str = ""

    spacecraft_altitude: Optional[float] = None

    center_latitude: Optional[float] = None

    center_longitude: Optional[float] = None

    # ======================================================
    # Image Information
    # ======================================================

    image_width: Optional[int] = None

    image_height: Optional[int] = None

    # ======================================================
    # File Locations
    # ======================================================

    xml_path: Optional[Path] = None

    data_path: Optional[Path] = None

    # ======================================================
    # Metadata Dictionary
    # ======================================================

    metadata: dict = field(default_factory=dict)

    # ======================================================
    # Processing Status
    # ======================================================

    loaded: bool = False

    validated: bool = False

    processed: bool = False

    # ======================================================
    # Dataset Summary
    # ======================================================

    def summary(self):
        """
        Print a scientific summary of the dataset.
        """

        print("\n")
        print("================================================")
        print("           DFSAR DATASET SUMMARY")
        print("================================================")

        print(f"Mission               : {self.mission}")

        print(f"Instrument            : {self.instrument}")

        print(f"Product Type          : {self.product_type}")

        print(f"Orbit Number          : {self.orbit_number}")

        print(f"Acquisition Time      : {self.acquisition_time}")

        print(f"Frequency Band        : {self.frequency_band}")

        print(f"Polarization          : {self.polarization}")

        print(f"Incidence Angle       : {self.incidence_angle}")

        print(f"Look Direction        : {self.look_direction}")

        print(f"Spacecraft Altitude   : {self.spacecraft_altitude}")

        print(f"Center Latitude       : {self.center_latitude}")

        print(f"Center Longitude      : {self.center_longitude}")

        print(f"Image Width           : {self.image_width}")

        print(f"Image Height          : {self.image_height}")

        print(f"Loaded                : {self.loaded}")

        print(f"Validated             : {self.validated}")

        print(f"Processed             : {self.processed}")

        print("================================================")
        print()

    # ======================================================
    # Dataset Validation
    # ======================================================

    def validate(self):
        """
        Validate the dataset before scientific processing.
        """

        if self.xml_path is None:
            raise ValueError("XML path is missing.")

        if self.data_path is None:
            raise ValueError("Radar data path is missing.")

        if self.frequency_band == "":
            raise ValueError("Frequency band missing.")

        if self.orbit_number is None:
            raise ValueError("Orbit number missing.")

        self.validated = True

        return True

    # ======================================================
    # Processing Flags
    # ======================================================

    def mark_loaded(self):
        """
        Mark dataset as successfully loaded.
        """

        self.loaded = True

    def mark_processed(self):
        """
        Mark dataset as processed.
        """

        self.processed = True