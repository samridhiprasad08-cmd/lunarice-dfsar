"""
===========================================================
PDS4 XML PARSER
===========================================================

Reads Chandrayaan-2 DFSAR PDS4 labels and extracts
scientific metadata required throughout the pipeline.

===========================================================
"""

import xml.etree.ElementTree as ET


class PDSParser:

    def __init__(self, xml_file):

        self.xml_file = xml_file

        self.tree = ET.parse(xml_file)

        self.root = self.tree.getroot()

    # -------------------------------------------------------
    # Generic XML Search
    # -------------------------------------------------------

    def find_text(self, tag):

        for element in self.root.iter():

            if element.tag.endswith(tag):

                return element.text

        return None

    # -------------------------------------------------------
    # Extract Scientific Metadata
    # -------------------------------------------------------

    def extract_metadata(self):

        metadata = {}

        # Mission Information

        metadata["mission"] = "Chandrayaan-2"

        metadata["instrument"] = "DFSAR"

        metadata["product_type"] = self.find_text("product_type")

        # Radar Information

        metadata["frequency_band"] = self.find_text("frequency_band")

        metadata["orbit_number"] = self.find_text("imaging_orbit_number")

        metadata["look_direction"] = self.find_text("look_direction")

        metadata["incidence_angle"] = self.find_text("incidence_angle")

        metadata["scene_start_time"] = self.find_text("scene_start_time")

        metadata["scene_end_time"] = self.find_text("scene_end_time")

        metadata["spacecraft_altitude"] = self.find_text(
            "spacecraft_altitude"
        )

        # Geometry

        metadata["centre_latitude"] = self.find_text(
            "centre_latitude"
        )

        metadata["centre_longitude"] = self.find_text(
            "centre_longitude"
        )

        metadata["upper_left_latitude"] = self.find_text(
            "upper_left_latitude"
        )

        metadata["upper_left_longitude"] = self.find_text(
            "upper_left_longitude"
        )

        metadata["upper_right_latitude"] = self.find_text(
            "upper_right_latitude"
        )

        metadata["upper_right_longitude"] = self.find_text(
            "upper_right_longitude"
        )

        metadata["lower_left_latitude"] = self.find_text(
            "lower_left_latitude"
        )

        metadata["lower_left_longitude"] = self.find_text(
            "lower_left_longitude"
        )

        metadata["lower_right_latitude"] = self.find_text(
            "lower_right_latitude"
        )

        metadata["lower_right_longitude"] = self.find_text(
            "lower_right_longitude"
        )

        # Radar Parameters

        metadata["pulse_length"] = self.find_text("pulse_length")

        metadata["pulse_bandwidth"] = self.find_text(
            "pulse_bandwidth"
        )

        metadata["sampling_frequency"] = self.find_text(
            "sampling_frequency"
        )

        metadata["pulse_repetition_frequency"] = self.find_text(
            "pulse_repetition_frequency"
        )

        metadata["radar_center_frequency"] = self.find_text(
            "radar_center_frequency"
        )

        metadata["number_of_polarizations"] = self.find_text(
            "num_polarizations"
        )

        return metadata

    # -------------------------------------------------------
    # Display Metadata
    # -------------------------------------------------------

    def print_metadata(self):

        metadata = self.extract_metadata()

        print()

        print("=" * 60)

        print("DFSAR PDS4 METADATA")

        print("=" * 60)

        for key, value in metadata.items():

            print(f"{key:30} : {value}")

        print("=" * 60)

        print()