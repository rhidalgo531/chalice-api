import logging
import logging.config
import s3fs
import json
import boto3
import json
import pandas as pd

from chalice import Chalice, Response
from modules.Services import DataService



app = Chalice(app_name='broadway-api')
app.debug = True

logging.config.fileConfig('logs.conf')
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logger.info("Initialized Logger")


broadway_dataset = pd.read_csv("s3://rmh391-broadway/yearly_gross.csv")


"""
    Return status information about the API and the end points available
"""
@app.route('/', methods=["GET"])
def status():
    dataset_schema = pd.io.json.build_table_schema(broadway_dataset)
    return Response(status_code=200, body=json.dumps(
        {"Current Status": "Humming Along",
            "Dataset Schema":dataset_schema,
            "Endpoints": [
                {"url":"/performances/html","query parameters": []},
                {"url":"/performances/broadway/{year}", "query parameters":  [
                    {"Name": "sort", "Use": "Sort by a dataframe column, as-is", "Example": "?sort=Name"},
                    {"Name": "limit", "Use":"Limit the amount of rows from dataset returned by server", "Example":"?limit=15"},
                    {"Name": "metric", "Use":"Calculate one of two metrics : sum of total gross, or count of total performances","Example":"?metric=gross/count"}
                ]}
            ]
        },indent=6, sort_keys=False), headers={"Content-Type":"application/json"})





"""
    This endpoint will return information regarding broadway performances

    In a larger API, performances would be the collection, and broadway could be one of multiple resources
    but for this broadway will be the only one


"""
@app.route('/performances/broadway/{year}', methods=["GET"])
def return_dataset_by_year(year):
    if app.current_request.method == "GET":
        query_params = app.current_request.query_params
        dataset = DataService.DataManager(broadway_dataset[broadway_dataset["Year"] == int(year)])
        if query_params is not None:
            dataset.apply_params(query_params)
        if dataset.status_code == 200 or dataset.status_code is None:
            response_body = json.dumps({
                "transformations_made": dataset.transformations_made,
                "data": dataset.data.to_json(orient="records", lines=True)
            }, sort_keys=True, indent=6)
            headers = {
                "Content-Type": "application/json"
            }
            return Response(status_code=200, body=response_body, headers=headers)
        else:
            return Response(status_code=dataset.status_code, body=dataset.data, headers={"Content-Type":"application/json"})


@app.route('/performances/html', methods=["GET"])
def return_html_object_location():
    return Response(
        status_code=200,
        headers={"Content-Type":"application/json"},
        body=json.dumps({
            "topic": "HTML Page Location on AWS S3 for third instruction",
            "AWS Availability": "Open to Public",
            "location":"https://s3.amazonaws.com/rmh391-broadway/index.html",
            "summary": "Simple index page with carousel made using bootstrap cdn"
            }, indent=6, sort_keys=True))
