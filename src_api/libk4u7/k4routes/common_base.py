import time

import tornado.web as tweb

from ..logutilz import simple_log as log


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class K4BaseHandler(tweb.RequestHandler):

    def initialize(self):

        self.req_start_time = time.time()

        log.dbg(f"New K4BaseHandler created.")

        self.set_header("Access-Control-Max-Age", "1000")




    def options(self, *args, **kwargs):
        """ Allow and implement HTTP OPTIONS request on all resources on this server. """

        self.respond()
