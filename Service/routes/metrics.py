''' Prometheus Mornitoring '''
import prometheus_client
from prometheus_client import Counter, Gauge, Summary, Histogram
from prometheus_client.core import  CollectorRegistry

REGISTRY = CollectorRegistry(auto_describe=False)
FLASK_REQUEST_LATENCY = Histogram('request_latency_seconds', 'Flask Request Latency', registry=REGISTRY)
FLASK_REQUEST_COUNT = Counter("requests_total", "Total count of requests", registry=REGISTRY)

import os, time
from flask import Response, request
from routes.ws_server import my_service

@my_service.route("/metrics")
def metrics():
    text = "# Process in {0}\n".format(os.getpid())
    return Response(text + prometheus_client.generate_latest(REGISTRY).decode(), mimetype="text/plain")


from flask import Response, request
def before_request():
    if request.path != "/metrics":
        request.start_time = time.time()
    else:
        request.start_time = 0

def after_request(response):
    if request.start_time != 0:
        request_latency = time.time() - request.start_time
        FLASK_REQUEST_LATENCY.observe(request_latency)
        FLASK_REQUEST_COUNT.inc()
    return response

my_service.before_request(before_request)
my_service.after_request(after_request)