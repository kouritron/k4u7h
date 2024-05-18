import os
import time
import random
import logging

import tornado.httpserver as tserver
import tornado.web as tweb
from tornado.ioloop import IOLoop

from libk4u7h.logutilz import simple_log as log
from libk4u7h import paramz


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    log.info(f"0====>>>>> serve_k4.py: starting 1 proc server ...\n")

    app = tweb.Application([], debug=False)

    http_server = tserver.HTTPServer(app)
    http_server.bind(paramz.K4_DEFAULT_PORT)
    http_server.start(1)
    IOLoop.current().start()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

if '__main__' == __name__:
    main()
