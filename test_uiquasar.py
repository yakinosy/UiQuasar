# test_uiquasar.py
"""
Tests for UiQuasar module.
"""

import unittest
from uiquasar import UiQuasar

class TestUiQuasar(unittest.TestCase):
    """Test cases for UiQuasar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UiQuasar()
        self.assertIsInstance(instance, UiQuasar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UiQuasar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
