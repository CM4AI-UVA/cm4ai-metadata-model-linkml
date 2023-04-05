"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from cm4ai_metadata_model_linkml.datamodel.cm4ai_metadata_model_linkml import FairscapeBaseModel, Dataset, Software, Computation

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            obj = yaml_loader.load(path, target_class=FairscapeBaseModel, Dataset, Software, Computation)
            assert obj
