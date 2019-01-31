import unittest
import s3fs
import pandas as pd
import DataService

url = 's3://rmh391-broadway/yearly_gross.csv'
data = pd.read_csv(url)
service = DataService.DataManager(data[data["Year"]==2003])

class TestDataRetrieval(unittest.TestCase):
    def test_load(self):
        self.assertEqual(type(data), pd.core.frame.DataFrame)


class TestDataService(unittest.TestCase):
    def test_limit(self):
        limit = 4
        service.limit_dataset(limit)
        dataset = service.data
        self.assertEqual(limit, len(dataset.index))

    def test_sort(self):
        service.sort_by_column("Gross")
        data = service.data
        self.assertEqual(True, not pd.Index(data["Gross"]).is_monotonic)



if __name__ == "__main__":
    unittest.main()
