import json
import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def config():
    config_path = Path(__file__).parent.parent / "config" / "settings.json"
    with open(config_path) as config_file:
        return json.load(config_file)
    