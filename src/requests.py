import requests
import curlify


class Requests(object):
    def __init__(self, print_curl, base_url):
        self.__print_curl = print_curl
        self.__base_url = base_url

    def __make_request(self, method, path, *args, **kwargs):
        url = f"{self.__base_url}{path}"

        if method == "get":
            response = requests.get(url, *args, **kwargs)
        else:
            raise RuntimeError(f"Unknown method '{method}'")

        self.response = response
        self.show_curl()
        return response

    def get(self, *args, **kwargs):
        return self.__make_request("get", *args, **kwargs)

    def show_curl(self):
        if self.__print_curl:
            print("\n", curlify.to_curl(self.response.request))

