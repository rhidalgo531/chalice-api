from chalice import Chalice, Response




app = Chalice(app_name='broadway-api')
app.debug = True


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
