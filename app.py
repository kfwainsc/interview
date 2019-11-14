import datetime

from flask import Flask, request
import jwt

from secrets import api_auth_token, jwt_secret_key
from utils import parse_date_time
import business

app = Flask(__name__)

def decode_auth_token(auth_token):
    # use jwt, jwt_secret_key
    pass

def encode_auth_token(user_id, name, email, scopes):
    # use jwt, jwt_secret_key
    # use the following payload:
    # { 'sub': user_id, 'name': name, 'email': email, 'scope': scopes }
    pass


def get_user_from_token():
    # use decode_auth_token above and flask.request imported above
    # should pull token from the Authorization header
    # Authorization: Bearer {token}
    # Where {token} is the token created by the login route
    pass


@app.route('/')
def status():
    return 'API Is Up'

@app.route('/user', methods=['GET'])
def user():
    # get the user from the auth/header/jwt and just return the user_id
    return {
        'user_id': ''
    }

@app.route('/login', methods=['POST'])
def login():
    # use use flask.request to get the json body and get the email and scopes property
    # use the business.login function to get the user data
    # return a the encoded json web token as a token property on the json response as in the format below
    # we're not actually validitating a password or anything because that would add unneeded complexity
    return {
        'token': ''
    }

@app.route('/widgets', methods=['GET'])
def widgets():
    # accept the following optional query parameters (using the the flask.request object to get the query params)
    # type, created_start, created_end
    # dates will be in iso format (2019-01-04T16:41:24+0200) and can be parsed using the parse_date_time function written and imported for you above
    # get the user ID from the auth/header
    # verify that the token has the widgets scope in the list of scopes


    # Using the requests library imported above send the following the following request,

    # GET https://example.com/widgets?user_id={user_id}
    # HEADERS
    # Authorization: Bearer {api_auth_token}

    # the api will return the data in the following format

    # [ { "id": 1, "type": "floogle", "created": "2019-01-04T16:41:24+0200" } ]
    # dates can again be parsed using the parse_date_time function

    # filter the results by the query parameters
    # return the data in the format below

    return {
        'total_widgets_own_by_user': 2,
        'matching_items': [
            {
                "id": 0,
                "type": "foo-bar",
                "type_label": "Foo Bar",  # replace dashes with spaces and capitalize words
                "created": datetime.datetime.now().isoformat(), # remember to replace
            }
        ]
    }


if __name__ == '__main__':
    app.run()