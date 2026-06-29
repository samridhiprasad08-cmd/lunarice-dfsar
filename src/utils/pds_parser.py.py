import xml.etree.ElementTree as ET


class PDSParser:

    def __init__(self, xml_file):

        self.xml_file = xml_file

        self.tree = ET.parse(xml_file)

        self.root = self.tree.getroot()


    def find_text(self, tag):

        for element in self.root.iter():

            if element.tag.endswith(tag):

                return element.text

        return None


    def extract_metadata(self):

        metadata = {}

        metadata["mission"] = self.find_text("name")

        metadata["product_type"] = self.find_text("product_type")

        metadata["frequency_band"] = self.find_text("frequency_band")

        metadata["incidence_angle"] = self.find_text("content")

        metadata["look_direction"] = self.find_text("look_direction")

        metadata["orbit_number"] = self.find_text("imaging_orbit_number")

        return metadata