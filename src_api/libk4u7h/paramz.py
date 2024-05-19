
import os
import subprocess as sp
from pathlib import Path

from .logutilz import simple_log as log

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# ord('k') + ord('4') == 159  --  Suggestion for default ports:
# - 15980  or 80 for the UI home page.
# - 15908  API

K4_DEFAULT_PORT = 159_80
TORNADO_DEBUG_MODE = True

REPO_ROOT_PATH = Path(sp.check_output("git rev-parse --show-toplevel", shell=True).decode()).resolve()
STATIC_DIR_PATH = (REPO_ROOT_PATH / 'build_tmp' / 'static').resolve()


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

log.info("k4 paramz subsystem initialized.")
log.info(f"repo root is at: {REPO_ROOT_PATH}")
log.info(f"static directory is set to: {STATIC_DIR_PATH}")



