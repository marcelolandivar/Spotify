import requests
import json

from .exceptions import BadRequestError
from .config import read_config
from .request_type import RequestType


def execute_request(url_template, auth, params, request_type=RequestType.GET, payload=()):
    """
    url_template: This is the template that will be used to build the URL to
    perform the request
    auth: Is the Authorization object
    params: It is a dict containing all the parameters that will be placed into
    the URL that we are going to perform the request on
    request: This is the request type; it can be GET or PUT
    payload: This is the data that may be sent together with the request
    """
    conf = read_config()
    params['base_url'] = conf.base_url
    url = url_template.format(**params)
    headers = {
        'Authorization': f'Bearer {auth.access_token}'
    }

    if request_type is RequestType.GET:
        response = requests.get(url, headers=headers)
    else:
        response = requests.put(url, headers=headers, data=json.dumps(payload))

        if not response.text:
            return response.text
    # Parsing the JSON result
    result = json.loads(response.text)

    # Check the status of the response
    if not response.ok:
        error = result['error']
        raise BadRequestError(
            f'{error["message"]} (HTTP {error["status"]}'
        )
    return result
