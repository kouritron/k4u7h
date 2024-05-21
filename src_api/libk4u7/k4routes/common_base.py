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




    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------- OPTIONS impl at k4base
    # ----- NOTE on implementing OPTIONS at top level
    # A well behaved OPTIONS implementation would tell caller, what methods are allowed on a given URI if any.
    # Tornado base request handler already has a method called get, post, put, .... that all subclasses would inherit.
    # but tornado internally assignes a _unimplemented thing. Tornado can figure out if you have supplied your own
    # get/post, otherwise it will default to 405 for those calls.
    # the cleanest soln i found for app code to figure out if subclass has supplied get/post or inherited from
    # tornado super is using something like "self.post.__func__ is not tweb.RequestHandler.post"
    def options(self):
        """ Allow and implement HTTP OPTIONS request on all resources on this server. """

        # this method needs to find out what is supported by its subclass for an actual resource and construct
        # a header like this that lists them:
        # self.set_header("Access-Control-Allow-Methods", "GET, PUT, OPTIONS")

        allowed_methods_list = []

        # --- check get
        if hasattr(self, 'get') and callable(getattr(self, 'get')):
            if self.get.__func__ is not tweb.RequestHandler.get:
                allowed_methods_list.append("GET")

        # --- check post
        if hasattr(self, 'post') and callable(getattr(self, 'post')):
            if self.post.__func__ is not tweb.RequestHandler.post:
                allowed_methods_list.append("POST")

        # --- check put
        if hasattr(self, 'put') and callable(getattr(self, 'put')):
            if self.put.__func__ is not tweb.RequestHandler.put:
                allowed_methods_list.append("PUT")

        # --- check delete
        if hasattr(self, 'delete') and callable(getattr(self, 'delete')):
            if self.delete.__func__ is not tweb.RequestHandler.delete:
                allowed_methods_list.append("DELETE")

        # --- check head
        if hasattr(self, 'head') and callable(getattr(self, 'head')):
            if self.head.__func__ is not tweb.RequestHandler.head:
                allowed_methods_list.append("HEAD")

        # --- check options
        if hasattr(self, 'options') and callable(getattr(self, 'options')):
            if self.options.__func__ is not tweb.RequestHandler.options:
                allowed_methods_list.append("OPTIONS")


        allowed_methods = ", ".join(allowed_methods_list)

        self.set_header("Access-Control-Allow-Methods", allowed_methods)

        log.dbg(f"{self.riid}|Handling [{self.request.method} {self.request.uri}] -- allow methods: {allowed_methods}")

        # OPTIONS has no content, and usually 204 is used here for OK
        self.set_status(HTTPStatus2xx.NO_CONTENT.value)
        self.finish()
