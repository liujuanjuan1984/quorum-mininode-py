import logging
import os

import requests

logger = logging.getLogger(__name__)


class HttpRequest:
    """Class for making http requests"""

    def __init__(
        self,
        chain_urls: list,
        timeout: int = 5,
        retries: int = 3,
    ):
        """
        Initializes the HttpRequest class
        chain_urls: list of dict of api_base and jwt_token
        """
        requests.adapters.DEFAULT_RETRIES = 5
        self.chain_urls = chain_urls
        self.current_chain_url = 0
        self.session = requests.Session()
        self.timeout = timeout
        self.retries = retries
        self.headers = {"Content-Type": "application/json"}
        self.session.headers.update(self.headers)

    def _request(
        self,
        method: str,
        endpoint: str,
        payload: dict = None,
    ):

        chain_url = self.chain_urls[self.current_chain_url]
        api_base = chain_url.get("baseurl")
        jwt_token = chain_url.get("jwt")
        if jwt_token:
            self.headers.update({"Authorization": f"Bearer {jwt_token}"})
            self.session.headers.update(self.headers)
        url = api_base + "/api/v1" + endpoint

        _no_proxy = os.getenv("NO_PROXY", "")
        if api_base not in _no_proxy:
            os.environ["NO_PROXY"] = ",".join([_no_proxy, api_base])

        try:
            for i in range(self.retries):
                try:
                    response = self.session.request(
                        method=method,
                        url=url,
                        json=payload,
                        timeout=self.timeout,
                        headers=self.headers,
                    )
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.RequestException as err:
                    logging.warning(
                        "HTTP request retry %s/%s: %s", i + 1, self.retries, err
                    )
        except requests.exceptions.RequestException as err:
            logging.warning(
                "HTTP request error (endpoint %s}): %s", self.current_chain_url, err
            )
            self.current_chain_url = (self.current_chain_url + 1) % len(self.chain_urls)
            return self._request(method, endpoint, payload)
        raise Exception("HTTP request error")

    def get(self, endpoint: str, payload: dict = None):
        return self._request("get", endpoint, payload)

    def post(self, endpoint: str, payload: dict = None):
        return self._request("post", endpoint, payload)
