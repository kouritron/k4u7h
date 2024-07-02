#!/bin/bash


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Ensure terminal launches bash instead of sh. that causes problem with tab char.
export SHELL=/bin/bash


# for a simple 0 $
export PS1="\$? $ "

export HISTFILE='/dev/null'
export HISTSIZE=40
# unset HISTFILE
unset LS_COLORS


export PYSPARK_PYTHON="python3"
export SPARK_LOCAL_IP="127.0.0.1"
export SPARK_OPTS="--master=local[20]"

export ZZPE_HOME="/root/zzpe"


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

cd $ZZPE_HOME

# x1ws is probably under /
pipenv run jupyter lab "/" --allow-root --no-browser --port 17732 --ip 127.0.0.1



# --- done, should be working
# cat /home/xk2/.local/lib/python3.10/site-packages/pyspark/version.py 
# jupyter toree install --user --spark_home=/home/xk2/.local/lib/python3.10/site-packages/pyspark

# -----
# python3 -c "import site; print(site.USER_SITE)"


# -----
# pipenv is gone, look into kdvq gh if you want the venv
# cd /home/xk2/.local/share/virtualenvs/
# you can rm -rf venvs here

