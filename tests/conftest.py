pytest_plugins = "pytester"

import os
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def original_datadir(request) -> Path:
    return Path(os.path.splitext(request.module.__file__)[0]) / request.function.__name__
