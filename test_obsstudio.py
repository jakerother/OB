# test_obsstudio.py
"""
Tests for OBSStudio module.
"""

import unittest
from obsstudio import OBSStudio

class TestOBSStudio(unittest.TestCase):
    """Test cases for OBSStudio class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OBSStudio()
        self.assertIsInstance(instance, OBSStudio)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OBSStudio()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
