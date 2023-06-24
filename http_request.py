import time
import httpx


class RequestThrottler:
    def __init__(self, rate_limit, interval):
        self.rate_limit = rate_limit  # Maximum number of requests allowed per interval
        self.interval = interval  # Time interval in seconds
        self.tokens = rate_limit  # Initially, set the token count to the rate limit
        self.last_request_time = time.time()  # Track the time of the last request

    def wait_for_token(self):
        while self.tokens <= 0:
            elapsed_time = time.time() - self.last_request_time
            if elapsed_time >= self.interval:
                self.tokens = self.rate_limit  # Reset token count after the interval
            else:
                time.sleep(0.1)  # Sleep for a short interval until tokens are available
        self.tokens -= 1

    def make_request(self, url, headers, data):
        self.wait_for_token()  # Wait until a token is available
        self.last_request_time = time.time()  # Update the last request time
        with httpx.Client() as client:
            response = client.post(url=url, headers=headers, data=data)
            return response.text
