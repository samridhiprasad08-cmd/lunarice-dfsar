from pathlib import Path
import yaml


class ConfigLoader:
    """
    Loads the project configuration from config.yaml.
    """

    def __init__(self, config_path="config.yaml"):

        self.config_path = Path(config_path)

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get(self, *keys):
        """
        Retrieve nested configuration values.

        Example:
            config.get("project", "name")
        """

        value = self.config

        for key in keys:
            value = value[key]

        return value

    def show_summary(self):

        print("=" * 60)
        print("PROJECT CONFIGURATION")
        print("=" * 60)

        print(f"Project      : {self.get('project', 'name')}")
        print(f"Version      : {self.get('project', 'version')}")
        print(f"Mission      : {self.get('project', 'mission')}")
        print(f"Instrument   : {self.get('project', 'instrument')}")

        print("=" * 60)