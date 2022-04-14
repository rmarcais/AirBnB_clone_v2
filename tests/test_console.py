#!/usr/bin/python3
import pycodestyle
import unittest
from models import BaseModel


class test_console(BaseModel):
    """Test class for db storage"""

    def test_pep8_console(self):
        """pep8 test"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/test_console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
