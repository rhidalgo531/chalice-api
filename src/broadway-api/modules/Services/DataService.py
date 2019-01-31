import pandas as pd

from chalice import Response


"""
    DataManager class will handle the data layer, applying transformations in a pipeline-like manner

"""
class DataManager(object):

    def __init__(self, data):
        self.data = data
        self.status_code = None


    def calculate_gross(self):
        self.data = self.data.groupby(["Name"])[["Gross"]].sum()

    def calculate_count(self):
        self.data = self.data.groupby(["Name"]).count()

    def sort_by_column(self, column):
        self.data = self.data.sort_values(by=column, ascending=False).reset_index()

    def limit_dataset(self, limit):
        self.data = self.data.head(limit)

    def apply_params(self, params):
        try:
            if "metric" in params:
                metric_type = params["metric"]
                if metric_type == "gross":
                    self.calculate_gross()
                elif metric_type == "count":
                    self.calculate_count()
                else:
                    self.status_code = 400
                    self.data = {"Error": "Ill-formed request. Allowed metric types are gross or count"}
            if "sort" in params:
                self.sort_by_column(params["sort"])
            if "limit" in params:
                self.limit_dataset(params["limit"])
        except Exception as e:
            print(e)
            self.status_code = 400

    def generate_simple_response(self):
        pass
