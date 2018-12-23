import requests
import curlify
import logging


def __make_request(method, *args, **kwargs):
    if method == "get":
        response = requests.get(*args, **kwargs)
    else:
        raise RuntimeError(f"Unknown method '{method}'")

    logging.debug(curlify.to_curl(response.request))
    print("\n", curlify.to_curl(response.request))
    return response


def get(*args, **kwargs):
    return __make_request("get", *args, **kwargs)
