import os
import time
import random
import logging

import tornado.web as tweb
import tornado.httpserver as tserver
from tornado.ioloop import IOLoop

from libk4u7.logutilz import simple_log as log
from libk4u7 import paramz
from libk4u7 import k4routes


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def init_3rd_party_loggers():
    """ Enable/disable loggers from tornado and/or other packages outside libk4u7 """
    
    loggers_list = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    for x in loggers_list:
        print(x)

    
    # print(logging.getLogger("tornado.application").disabled)
    # logging.getLogger("tornado.application").disabled = True


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    log.info(f"*** serve_k4.py: starting 1 proc server ...\n")

    init_3rd_party_loggers()

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
