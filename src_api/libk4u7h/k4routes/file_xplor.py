import os
import tornado.web as tweb
from .common_base import K4BaseHandler






# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class IndexHandler(K4BaseHandler):

    def get(self):
        self.write(f"Hi, your number is: {os.urandom(6).hex()}")











