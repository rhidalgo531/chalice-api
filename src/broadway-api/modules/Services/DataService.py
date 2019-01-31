import pandas as pd

from chalice import Response


"""
    DataManager class will handle the data layer, applying transformations in a pipeline-like manner

"""
class DataManager(object):

    def __init__(self, data):
        self.data = data
        self.status_code = None
        self.transformations_made = 0


    def calculate_gross(self):
        self.data = self.data.groupby(["Name"])[["Gross"]].sum().sort_values(['Gross'], ascending=False).reset_index()
        self.transformations_made += 1

    def calculate_count(self):
        self.data = self.data.groupby(["Name"]).size().reset_index(name='Performances')
        self.transformations_made += 1

    def sort_by_column(self, column):
        self.data = self.data.sort_values(by=column, ascending=False).reset_index()
        self.transformations_made += 1

    def limit_dataset(self, limit):
        self.data = self.data.head(int(limit))
        self.transformations_made += 1

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
            self.status_code = 200
        except Exception as e:
            print(e)
            self.status_code = 400
