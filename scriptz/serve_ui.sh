#!/bin/bash

# ord('k') + ord('4') == 159  --  Suggestion for default ports:
# - 15980  or 80 for the UI home page.
# - 15908  API

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


REPO_ROOT=$(git rev-parse --show-toplevel)
cd $REPO_ROOT
# printf "pwd: $(pwd)\n\n"



python3 -m http.server 15980 --bind 127.0.0.1 --directory ./build_tmp/




