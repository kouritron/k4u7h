
import os
import time
import subprocess as sp
from pathlib import Path

from .logutilz import simple_log as log

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# ord('k') + ord('4') == 159  --  Suggestion for default ports:
# - 15980  or 80 for the UI home page.
# - 15908  API

K4_DEFAULT_PORT = 159_80
TORNADO_DEBUG_MODE = False

REPO_ROOT_PATH = Path(sp.check_output("git rev-parse --show-toplevel", shell=True).decode().strip()).resolve()
STATIC_DIR_PATH = (REPO_ROOT_PATH / 'build_ui' / 'static').resolve()
FAVICON_PATH = (STATIC_DIR_PATH / 'favicon.ico').resolve()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# A tiny sleep between autoreloads is useful. Also gives a visual cue of the reload.
sp.call("clear", shell=True)
time.sleep(.3)

log.info(f"k4 paramz subsystem initialized. random session id: {os.urandom(8).hex()}")
log.info(f"repo root is at: {REPO_ROOT_PATH}")
log.info(f"static directory is set to: {STATIC_DIR_PATH}")
log.info(f"favicon is set to: {FAVICON_PATH}")
log.info(f"favicon file exists: {FAVICON_PATH.exists()}")


