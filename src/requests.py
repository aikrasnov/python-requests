import requests
import curlify


def __make_request(method, *args, **kwargs):
    if method == "get":
        response = requests.get(*args, **kwargs)
    else:
        raise RuntimeError(f"Unknown method '{method}'")

    print("\n", curlify.to_curl(response.request))
    return response


def get(*args, **kwargs):
    return __make_request("get", *args, **kwargs)
