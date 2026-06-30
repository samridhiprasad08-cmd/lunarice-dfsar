from src.utils.config_loader import ConfigLoader

config = ConfigLoader()

config.show_summary()

print()

print("Logs folder:")
print(config.get("paths", "logs"))