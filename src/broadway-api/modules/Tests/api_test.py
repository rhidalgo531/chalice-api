import unittest
import s3fs
import pandas as pd


class TestDataService(unittest.TestCase):

    def test_limit(self):
        pass


class TestDataRetrieval(unittest.TestCase):
    def test_load(self):
        url = 's3://rmh391-broadway/yearly_gross.csv'
        data = pd.read_csv(url)
        self.assertEqual(type(data), pd.core.frame.DataFrame)
