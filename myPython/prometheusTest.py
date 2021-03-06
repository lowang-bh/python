#!/usr/bin/env python

import random
import time
from prometheus_client import start_http_server, Summary
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    # start_http_server(8000)
    # # Generate some requests.
    # while True:
    #     process_request(random.random())


    registry = CollectorRegistry()
    g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)
    g.set_to_current_time()
    push_to_gateway('10.143.248.208:9091', job='batchA', registry=registry)
