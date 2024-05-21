""" 
K4BaseHandler is super class for all HTTP request handlers in K4.
StaticHandler and some other tornado built-ins do not inherit from this, all other route handlers should. 
"""

import os
import time

import tornado.web as tweb

from ..logutilz import simple_log as log
from ..http_codez import HTTPStatus2xx


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class K4BaseHandler(tweb.RequestHandler):

    def initialize(self):

        self.req_start_time = time.time()
        self.riid = os.urandom(8).hex()
        # riid -> req internal id

        log.dbg(f"{self.riid}|K4BaseHandler.initialize():  [{self.request.method} {self.request.uri}]")

        # CORS is not needed yet. maybe later.
        # self.set_header("Access-Control-Max-Age", "1000")


    # ----- NOTE on implementing OPTIONS at top level
    # its tempting but not super clean.
    # A well behaved OPTIONS implementation would tell the client, what methods are allowed on this resource if any.
    # Tornado base request handler already has a method called get, post, put, .... that all subclasses would inherit.
    # but tornado internally assignes a _unimplemented and tornado can figure out if you have supplied your get/post,
    # otherwise it will default to 405 for those calls
    # app code would not be pretty if it meddles with those internal tornado types. but maybe alternative is worse.

    def options(self):
        """ Allow and implement HTTP OPTIONS request on all resources on this server. """

        # this method needs to find out what is supported by its subclass for an actual resource and construct
        # a header like this that lists them:
        # self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

        allowed_methods_list = []

        for http_method in ["get", "post", "put", "delete", "head", "options"]:
            if hasattr(self, http_method) and callable(getattr(self, http_method)):
                allowed_methods_list.append(http_method.upper())

        allowed_methods = ", ".join(allowed_methods_list)

        self.set_header("Access-Control-Allow-Methods", allowed_methods)

        log.dbg(f"{self.riid}|Handling [{self.request.method} {self.request.uri}] -- Allowed: {allowed_methods}")

        # OPTIONS has no content, and usually 204 is used here for OK
        self.set_status(HTTPStatus2xx.NO_CONTENT.value)
        self.finish()