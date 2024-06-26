#!/bin/bash
# set -x for debugging
# set -e would exit as soon as first non-zero is encountered.

# K4 default port: 159_80

REPO_ROOT=$(git rev-parse --show-toplevel)
cd $REPO_ROOT


# to see help for POST
# curl -h POST


# -i or --include to see headers and extra info
# -L or --location  to follow redirects

# --head for HTTP HEAD method
# --get should be same -X GET

# -w "\n"  to always append a newline

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------





# curl --get http://127.0.0.1:15980/
# curl --get http://127.0.0.1:15980/static/k4u7_ui_bundle.js


# curl --head http://127.0.0.1:15980/static/k4u7_ui_bundle.js
# curl --head http://127.0.0.1:15980/favicon.ico

# curl --get --include --location http://127.0.0.1:15980/favicon.ico
# curl --get --include --location http://127.0.0.1:15980/



# curl -X POST http://127.0.0.1:15980/ -H "Content-Type: application/json" --data '{"p1": "foo", "p2": "bar"}'


curl -i -w "\n" -X POST http://127.0.0.1:15980/dx_api/sha256 -H "Content-Type: application/json" -d '{"msg": "hello"}'
curl -i -w "\n" -X POST http://127.0.0.1:15980/dx_api/sha512 -H "Content-Type: application/json" -d '{"msg": "hello"}'




# curl --get -i -w "\n" http://127.0.0.1:15980/dx_api/sha256?msg=hello+world




exit 0


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------














