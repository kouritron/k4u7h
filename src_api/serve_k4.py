import os
import time
import random
import logging

import tornado.web as tweb
import tornado.httpserver as tserver
from tornado.ioloop import IOLoop as TorIOLoop

from libk4u7.logutilz import simple_log as log
from libk4u7 import paramz
from libk4u7 import k4routes


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def init_3rd_party_loggers():
    """ Enable/disable loggers from tornado and/or other packages outside libk4u7 """

    logging.getLogger("tornado.application").setLevel(logging.INFO)
    logging.getLogger("tornado.general").setLevel(logging.INFO)
    logging.getLogger("tornado.access").setLevel(logging.INFO)
    logging.getLogger("tornado").setLevel(logging.INFO)

    loggers_list = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for x in loggers_list:
        print(x)

    # by default most are enabled, and set to WARNING level. Some of the loggers:
    # concurrent concurrent.futures asyncio tornado.access tornado tornado.application tornado.general

    # To disable
    # logging.getLogger("tornado.application").disabled = True


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():

    init_3rd_party_loggers()

    # ----- setup tornado app
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

    k4app = tweb.Application(exposed_routes, **tor_settings)

    # ----- start listening
    log.info(f"\n\n\n*** serve_k4.py: starting 1 proc server ...\n")

    # This works fine w/ both single and multi process servers.
    # Just pass the number of pids to start()
    http_server = tserver.HTTPServer(k4app)
    http_server.bind(paramz.K4_DEFAULT_PORT)
    http_server.start(1)

    TorIOLoop.current().start()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

if '__main__' == __name__:
    main()
