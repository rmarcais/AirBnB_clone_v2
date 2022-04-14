#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

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

