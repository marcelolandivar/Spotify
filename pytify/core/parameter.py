from urllib.parse import urlencode


def validate_params(params, required=None):
    """"
    The validate_params function is used to identify whether there
    are parameters that are required for a certain operation, but
    they haven't been supplied.
    """
    if required is None:
        return

    partial = {x: x in params.keys() for x in required}
    not_supplied = [x for x in partial.keys() if not partial[x]]

    if not_supplied:
        msg = f'The parameter(s) {", ".join(not_supplied)} are required'
        raise AttributeError(msg)


def prepare_params(params, required=None):
    """
    The prepare_params function first calls validate_params to make sure that
    all the parameters have been supplied and to also join all the parameters
    together so they can be easily appended to the URL query string.
    """

    if params is None and required is not None:
        msg = f'The parameter(s) {", ".join(required)} are required'
        raise ValueError(msg)
    elif params is None and required is None:
        return ''
    else:
        validate_params(params, required)

    query = urlencode('&'.join([f'{key}={value}' for key, value in params.items()]))

    return f'?{query}'




