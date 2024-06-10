import os
import tornado.web as tweb
from .common_base import K4BaseHandler


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class Handler_SHA256(K4BaseHandler):

    def get(self):
        self.write(f"Hi, your number is: {os.urandom(6).hex()}\n")

    # def post(self):
    #     self.write(f"Hi, your number is: {os.urandom(6).hex()}\n")


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class Handler_SHA3_256(K4BaseHandler):

    def get(self):
        self.write(f"Hi, your number is: {os.urandom(6).hex()}\n")






