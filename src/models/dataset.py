from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class DFSARDataset:

    mission: str
    instrument: str

    product_type: str

    frequency_band: str

    polarization: str

    orbit_number: int

    acquisition_time: str

    incidence_angle: float

    look_direction: str

    spacecraft_altitude: float

    center_latitude: float

    center_longitude: float

    image_width: int

    image_height: int

    xml_path: Path

    data_path: Path

    metadata: dict

    processed=False