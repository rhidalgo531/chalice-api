import unittest
import s3fs
import pandas as pd

url = 's3://rmh391-broadway/yearly_gross.csv'
data = pd.read_csv(url)

class TestDataService(unittest.TestCase):

    def test_limit(self):

        pass


class TestDataRetrieval(unittest.TestCase):
    def test_load(self):
        self.assertEqual(type(data), pd.core.frame.DataFrame)
