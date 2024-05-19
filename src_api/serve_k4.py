import os
import time
import random
import logging

import tornado.web as tweb
import tornado.httpserver as tserver
from tornado.ioloop import IOLoop

from libk4u7h.logutilz import simple_log as log
from libk4u7h import paramz
from libk4u7h import k4routes


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    log.info(f"*** serve_k4.py: starting 1 proc server ...\n")

    tor_settings = {
        # Enable debug mode for better error messages, disable useless autoreload.
        "debug": True,
        "autoreload": False,
    }


    exposed_routes = [
        (r"/", k4routes.core.IndexHandler),
        (r"/favicon\.ico", k4routes.redirections.RedirectFaviconHandler),
        (r"/static/(.*)", tweb.StaticFileHandler, {
            "path": str(paramz.STATIC_DIR_PATH)
        }),
    ]

    app = tweb.Application(exposed_routes, **tor_settings)

    # This works fine w/ both single and multi process servers. Just pass the number of pids to start()
    http_server = tserver.HTTPServer(app)
    http_server.bind(paramz.K4_DEFAULT_PORT)
    http_server.start(1)

    IOLoop.current().start()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

if '__main__' == __name__:
    main()
