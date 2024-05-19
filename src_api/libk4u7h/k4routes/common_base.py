import tornado.web as tweb

from ..logutilz import simple_log as log


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class K4BaseHandler(tweb.RequestHandler):

    def options(self, *args, **kwargs):
        """ Allow and implement HTTP OPTIONS request on all resources on this server. """

        self.respond()
