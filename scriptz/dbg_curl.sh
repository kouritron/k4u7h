#!/bin/bash


# K4 default port: 159_80

REPO_ROOT=$(git rev-parse --show-toplevel)
cd $REPO_ROOT


# to see help for POST
# curl -h POST


# -i or --include to see headers and extra info
# -L or --location  to follow redirects

# --head for HTTP HEAD method
# --get should be same -X GET



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------





# curl --get http://127.0.0.1:15980/
# curl --get http://127.0.0.1:15980/static/k4u7h_ui_bundle.js


# curl --head http://127.0.0.1:15980/static/k4u7h_ui_bundle.js
# curl --head http://127.0.0.1:15980/favicon.ico

curl --get --include http://127.0.0.1:15980/favicon.ico



# curl -X POST http://127.0.0.1:15980/ -H "Content-Type: application/json" --data '{"p1": "foo", "p2": "bar"}'








# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------














