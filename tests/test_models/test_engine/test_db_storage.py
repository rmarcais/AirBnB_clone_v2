#!/usr/bin/python3
import pycodestyle
import unittest
from models import BaseModel


class test_db_storage(BaseModel):
    """Test class for db storage"""

    def test_pep8_DBStorage(self):
        """pep8 test"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
