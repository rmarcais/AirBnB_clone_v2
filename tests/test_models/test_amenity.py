#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle
import os


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def teardown(self):
        """ """
        try:
            os.remove()
        except Exception:
            pass

    def test_name2(self):
        """ """
        self.assertEqual(type(self.name), str)
    
    def test_pep8_DBStorage(self):
        """pep8 test"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


    def test_save(self):
        """ """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_ad, self.amenity.updated_at)

    def test_attr(self):
        """ """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

