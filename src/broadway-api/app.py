import logging
import logging.config
import s3fs
import json
import boto3

from chalice import Chalice, Response
import pandas as pd



app = Chalice(app_name='broadway-api')
app.debug = True

logging.config.fileConfig('logs.conf')
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logger.info("Initialized Logger")


broadway_dataset = pd.read_csv("s3://rmh391-broadway/yearly_gross.csv")

@app.route('/')
def index():
    return {'hello': 'world'}





"""
    This endpoint will return information regarding broadway performances

    In a larger API, performances would be the collection, and broadway could be one of multiple resources
    but for this broadway will be the only one


"""
@app.route('/performances/broadway/{year}', methods=["GET"]):
def return_dataset_by_year(year):
    if app.current_request.method == "GET":




# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
