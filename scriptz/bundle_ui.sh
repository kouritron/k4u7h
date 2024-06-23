#!/bin/bash


REPO_ROOT=$(git rev-parse --show-toplevel)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
cd $REPO_ROOT
echo "dropping old build ..."
rm -rf $REPO_ROOT/build_ui

# sleep 3
echo "making new bundle ..."
mkdir -p $REPO_ROOT/build_ui/static

cp $REPO_ROOT/src_ui/index.html $REPO_ROOT/build_ui/index.html 
cp $REPO_ROOT/src_ui/assets/favicon.ico $REPO_ROOT/build_ui/favicon.ico
cp $REPO_ROOT/src_ui/assets/favicon.ico $REPO_ROOT/build_ui/static/favicon.ico



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
cd $REPO_ROOT/src_ui
# printf "pwd: $(pwd)\n\n"


# for prod minify
# esbuild app.jsx --bundle --minify --target=chrome85,firefox80

esbuild app.jsx --bundle --sourcemap --outfile=$REPO_ROOT/build_ui/static/k4u7_ui_bundle.js



# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------





