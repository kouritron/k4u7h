'''
dx_api are just demos and example routes. dont rename these if you actually find the functionality useful. Keep this
file just a demonstrator 

'''

import os
import json
import hashlib

# import tornado.web as tweb
from .common_base import K4BaseHandler
from ..http_codez import HTTP_4xx


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class Handler_ComputeMD(K4BaseHandler):

    def compute_msg_digest(self, msg: str):
        req_path = self.request.path
        req_path = req_path.lower()

        # careful if you support both hmac_sha256 and sha256. you might want to use initialize method,
        # and pass route_name along from where the route was registered.

        if req_path.endswith("dx_api/sha256"):
            hex_fp = hashlib.sha256(msg.encode('utf-8')).hexdigest()

        if req_path.endswith("dx_api/512"):
            hex_fp = hashlib.sha512(msg.encode('utf-8')).hexdigest()

        if req_path.endswith("dx_api/sha3_256"):
            hex_fp = hashlib.sha3_256(msg.encode('utf-8')).hexdigest()

        print(hex_fp)

        # ---
        self.write({"msg": msg, "sha256_fp": hex_fp})
        self.finish()

    # ------------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------- Xtract args, filter invalid requests
    def get(self):
        msg = self.get_argument('msg', None)
        if msg is None:
            self.set_status(HTTP_4xx.BAD_REQUEST.value)
            self.finish()
            return

        # --- fp msg
        self.compute_msg_digest(msg)

    def post(self):

        msg = None
        try:
            req_body_dict = json.loads(self.request.body)
            msg = req_body_dict.get('msg', default=None)
        except Exception:
            self.set_status(HTTP_4xx.BAD_REQUEST.value)
            self.write({"error": "bad request"})
            return

        # ---
        if msg is None:
            self.set_status(HTTP_4xx.BAD_REQUEST.value)
            self.write({"error": "bad request"})
            return

        # --- fp msg
        self.compute_msg_digest(str(msg))


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

#   self.write(f"Hi, your number is: {os.urandom(6).hex()}\n")
