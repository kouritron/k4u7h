import os
import tornado.web as tweb
from .common_base import K4BaseHandler

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


class RedirectFaviconHandler(K4BaseHandler):

    def get(self):
        self.redirect("/static/favicon.ico")

    def head(self):
        self.redirect("/static/favicon.ico")
